from sentence_transformers import SentenceTransformer
import numpy as np
import os
import hashlib
import json
from sklearn.metrics.pairwise import cosine_similarity
import sys

def build_corpus_and_hashes(directory):
    corpus = []
    filenames = []
    hashes = {}
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            with open(os.path.join(directory, filename), 'r') as f:
                content = f.read()
                corpus.append(content)
                filenames.append(filename.replace('.md', ''))  # Remove the .md extension here
                md5_hash = hashlib.md5(content.encode()).hexdigest()
                hashes[filename.replace('.md', '')] = md5_hash
    return filenames, corpus, hashes


def save_embeddings_and_hashes(embeddings, filenames, hashes, embeddings_file, hashes_file):
    np.savez(embeddings_file, **embeddings)
    with open(hashes_file, 'w') as f:
        json.dump(hashes, f)

def load_embeddings_and_hashes_old(embeddings_file, hashes_file, indices_file):
    try:
        embeddings_array = np.load(embeddings_file)
    except FileNotFoundError:
        embeddings_array = np.array([])

    try:
        with open(hashes_file, 'r') as f:
            hashes = json.load(f)
    except FileNotFoundError:
        hashes = {}

    try:
        with open(indices_file, 'r') as f:
            indices = json.load(f)
    except FileNotFoundError:
        indices = {}

    # Convert numpy array to dictionary using indices
    embeddings = {filename: embeddings_array[idx] for filename, idx in indices.items()}

    return embeddings, hashes

def load_embeddings_and_hashes(embeddings_file, hashes_file):
    embeddings = None

    try:
        embeddings = np.load(embeddings_file, allow_pickle=True)
        # 'allow_pickle=True' is added just in case the numpy arrays are not able to be loaded due to the numpy version
    except FileNotFoundError:
        print(f"Embeddings file not found: {embeddings_file}")

    try:
        with open(hashes_file, 'r') as f:
            hashes = json.load(f)
    except FileNotFoundError:
        hashes = {}

    return embeddings, hashes




#def build_and_save_embeddings(directory, model_name, embeddings_path, indices_path, hashes_path):
#    corpus, filenames, hashes = build_corpus_and_hashes(directory)
#    model = SentenceTransformer(model_name)
#    embeddings = model.encode(corpus, convert_to_tensor=True)
#    np.save(embeddings_path, embeddings.cpu().numpy())
#    indices = {filename: index for index, filename in enumerate(filenames)}
#    with open(indices_path, 'w') as f:
#        json.dump(indices, f)
#    with open(hashes_path, 'w') as f:
#        json.dump(hashes, f)
#    return filenames, embeddings, model

def build_and_save_embeddings(directory, model_name, embeddings_path, indices_path, hashes_path):
    filenames, corpus, hashes = build_corpus_and_hashes(directory)  # Here filenames is now a list of file names
    model = SentenceTransformer(model_name)
    embeddings = model.encode(corpus, convert_to_tensor=True)
    np.save(embeddings_path, embeddings.cpu().numpy())
    indices = {filename: index for index, filename in enumerate(filenames)}
    with open(indices_path, 'w') as f:
        json.dump(indices, f)
    with open(hashes_path, 'w') as f:
        json.dump(hashes, f)
    return filenames, embeddings, model






def get_semantic_scores(query, model, embeddings, filenames, indices):
    query_vec = model.encode([query], convert_to_tensor=True)[0].cpu().numpy()  # Convert tensor to numpy
    scores = []
    for filename in filenames:
        score = cosine_similarity(query_vec.reshape(1, -1), embeddings[indices[filename]].reshape(1, -1))[0][0] 
        scores.append((filename, score))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:5]




if __name__ == "__main__":
    directory = "./saved_concepts"
    model_name = 'all-MiniLM-L6-v2'
    embeddings_path = 'embeddings.npy'
    indices_path = 'indices.json'
    hashes_path = 'hashes.json'

    if not os.path.exists(directory):
        os.makedirs(directory)

    filenames, embeddings, model = build_and_save_embeddings(directory, model_name, embeddings_path, indices_path, hashes_path)

    # Load the indices dictionary
    with open(indices_path, 'r') as f:
        indices = {k: int(v) for k, v in json.load(f).items()}

    # Check if a query was passed as command-line argument
    if len(sys.argv) > 1:
        query = sys.argv[1]
        scores = get_semantic_scores(query, model, embeddings, filenames, indices)

        # Print the scores in console
        print("Query: ", query)
        print("Results:")
        for filename, score in scores:
            print(filename, score)
    else:
        print("Please provide a search query as a command-line argument.")

