from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import os
import sys

def build_corpus(directory):
    corpus = []
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            with open(os.path.join(directory, filename), 'r') as f:
                corpus.append(f.read())
                filenames.append(filename.replace('.md', ''))
    return corpus, filenames

def build_tfidf_index(directory):
    corpus, filenames = build_corpus(directory)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    return vectorizer, tfidf_matrix, filenames

def get_scores(query, vectorizer, tfidf_matrix, filenames):
    query_vec = vectorizer.transform([query])
    cosine_similarities = linear_kernel(query_vec, tfidf_matrix).flatten()
    related_docs_indices = cosine_similarities.argsort()[:-5:-1]
    scores = [(filenames[i], cosine_similarities[i]) for i in related_docs_indices if cosine_similarities[i] > 0]
    return scores

if __name__ == "__main__":
    directory = "./saved_concepts"
    vectorizer, tfidf_matrix, filenames = build_tfidf_index(directory)

    # Check if a query was passed as command-line argument
    if len(sys.argv) > 1:
        query = sys.argv[1]
        scores = get_scores(query, vectorizer, tfidf_matrix, filenames)

        # Print the scores in console
        print("Query: ", query)
        print("Results:")
        for filename, score in scores:
            print(filename, score)
    else:
        print("Please provide a search query as a command-line argument.")

