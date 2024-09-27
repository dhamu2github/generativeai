# searchs_combined.py

import numpy as np
from scipy.spatial.distance import cdist
from sentence_transformers import SentenceTransformer
from semantic_search import create_qdrant_collection,upload_vectors_to_qdrant_collection,semantic_search_qdrant
from keyword_search import keyword_search

# Load the pre-trained model for dense vector generation
model = SentenceTransformer("all-MiniLM-L6-v2") # You can use a different model here

# Reciprocal Rank Fusion
def reciprocal_rank_fusion(semantic_ranks, keyword_ranks, max_rank=60):
    rrf_scores = {}
    for i, doc_id in enumerate(semantic_ranks):
        doc_id = rrf_scores.get(doc_id, 0) + 1 / (max_rank + i)
    for i, doc_id in enumerate(keyword_ranks):
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + 1 / (max_rank + i)
    
    combined_ranks = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)
    return [doc_id for doc_id, score in combined_ranks]



#Following code for unit testing
if __name__ == "__main__":
    #sample data for testing
    documents = ["Artificial Intelligence","Machine learning","Neural Network","A dog is not feeling well","Generative AI"]
    #sample query
    #query = "Neural Network"
    query = "veterinary"

   #Load Semantic search using with DB
    create_qdrant_collection()
    upload_vectors_to_qdrant_collection(documents)
    semantic_results, semantic_scores = semantic_search_qdrant(query) 

    #Keyword Seach call 
    keyword_results, keyword_scores = keyword_search(query, documents)

    # Combine results using RRF
    combined_results = reciprocal_rank_fusion(semantic_results, keyword_results)
    

    for i, doc_id in enumerate(combined_results):
        print(f"Document {doc_id + 1}: {documents[doc_id]}")