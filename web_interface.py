from flask import Flask, render_template, request, url_for
from chat_generator import generate_chat, write_to_file
import mistune
import os
import re
import urllib.parse
from pathlib import Path

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

