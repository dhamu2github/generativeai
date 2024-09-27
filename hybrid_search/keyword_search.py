# keyword_search.py

import numpy as np
from scipy.spatial.distance import cdist
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi


# Load the pre-trained model for dense vector generation
model = SentenceTransformer("all-MiniLM-L6-v2")  # You can use a different model here


# Function for Keyword Search using BM25
def keyword_search(query, documents, top_k=5):
    tokenized_docs = [doc.split() for doc in documents]
    bm25 = BM25Okapi(tokenized_docs)
    scores = bm25.get_scores(query.split())
    results = np.argsort(scores)[::-1][:top_k]
    return results, scores[results]

#Following code for unit testing
if __name__ == "__main__":
    #sample data for testing
    documents = ["Artificial Intelligence","Machine learning","Neural Network","A dog is not feeling well","Generative AI"]
    #sample query
    query = "Neural Network"

    keyword_results, keyword_scores = keyword_search(query, documents)
    for i, doc_id in enumerate(keyword_results):
        print(f"Document {doc_id + 1}: {documents[doc_id]} (Score: {keyword_scores[i]:.4f})")


