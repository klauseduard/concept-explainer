#!/usr/bin/env python3

from sentence_transformers import SentenceTransformer
from flask import Flask, render_template, request, url_for
from flask_httpauth import HTTPBasicAuth
from chat_generator import generate_chat, write_to_file
import mistune
import os
import re
import json
import urllib.parse
from pathlib import Path
from search_tfidf import build_tfidf_index, get_scores
from search_semantic import load_embeddings_and_hashes, build_corpus_and_hashes, get_semantic_scores


app = Flask(__name__)

# create the authentication object
auth = HTTPBasicAuth()

# create corpus and tf-idf matrix once when server starts
vectorizer, tfidf_matrix, filenames = build_tfidf_index("./saved_concepts")


# semantic search stuff
model_name = 'all-MiniLM-L6-v2'
embeddings_path = 'embeddings.npy'
hashes_path = 'hashes.json'
directory = "./saved_concepts"
indices_path = 'indices.json'

model = SentenceTransformer(model_name)
#embeddings, hashes = load_embeddings_and_hashes(embeddings_path, hashes_path, indices_path)
embeddings, hashes = load_embeddings_and_hashes(embeddings_path, hashes_path)

ss_filenames, corpus, old_hashes = build_corpus_and_hashes(directory)
with open(indices_path, 'r') as f:
    indices = json.load(f)


# define the authentication verification function
@auth.verify_password
def verify_password(username, password):
    return username == os.getenv('AUTH_USERNAME') and password == os.getenv('AUTH_PASSWORD')

@app.before_request
def before_request():
    if os.getenv('REQUIRE_AUTH') == 'True':
        return auth.login_required(lambda: None)()


@app.route('/', methods=['GET', 'POST'])
def index():
    concept = request.args.get('concept', "Software architecture")
    specialist_role = request.args.get('specialist_role', "Software architect")
    target_audience = request.args.get('target_audience', "Manager without much technical background")
    additional_context = request.args.get('additional_context', None)

    if request.method == 'POST':
        concept = request.form.get('concept', concept)
        specialist_role = request.form.get('specialist_role', specialist_role)
        target_audience = request.form.get('target_audience', target_audience)
        additional_context = request.form.get('additional_context', additional_context)
        chat_content = generate_chat(concept, specialist_role, target_audience, additional_context)
        if chat_content:
            html_content = mistune.markdown(chat_content)
            write_to_file(concept, chat_content)
            return render_template('template.html', result=html_content, concept=concept, specialist_role=specialist_role, target_audience=target_audience, additional_context=additional_context)
        else:
            return render_template('template.html', error="Error generating chat.", concept=concept, specialist_role=specialist_role, target_audience=target_audience, additional_context=additional_context)

    return render_template('template.html', concept=concept, specialist_role=specialist_role, target_audience=target_audience, additional_context=additional_context)


@app.route('/concepts')
def concepts():
    # Get a list of all .md files in the explanations directory
    explanations_dir = Path('saved_concepts')
    concept_files = explanations_dir.glob('*.md')
    # Extract the concept names from the file names
    concepts = sorted([file.stem for file in concept_files], key=str.lower)
    return render_template('concepts.html', concepts=concepts)


@app.route('/concepts/<concept>', methods=['GET'])
def concept(concept):
    file_path = Path('saved_concepts') / f"{concept}.md"
    if file_path.exists():
        with open(file_path, 'r') as file:
            content = file.read()
            regex_pattern = r'\[(.*?)\]\((.*?)\)'

            def replace_url(match):
                url = match.group(2)
                modified_url = url.replace('?', '/?')
                return f'[{match.group(1)}]({modified_url})'

            content = re.sub(regex_pattern, replace_url, content)

            html_content = mistune.markdown(content)
            return render_template('concept.html', concept=concept, explanation=html_content)
    else:
        abort(404, description="Concept not found.")


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    print(type(query))
    print(query)
    scores = get_scores(query, vectorizer, tfidf_matrix, filenames)
    return render_template('search.html', scores=scores, query=query)


#@app.route('/search_semantic', methods=['GET'])
#def search_semantic():
#    query = request.args.get('query', '')
#    scores = []
#    if query:
#        scores = get_scores(query, model, embeddings, filenames)
#    return render_template('search_semantic.html', scores=scores, query=query)

@app.route('/search_semantic', methods=['GET'])
def search_semantic():
    query = request.args.get('query', '')
    scores = []
    if query:
        scores = get_semantic_scores(query, model, embeddings, ss_filenames, indices)
    return render_template('search_semantic.html', scores=scores, query=query)




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

