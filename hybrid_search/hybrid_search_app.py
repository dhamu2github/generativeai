# hybrid_search_app.py

import streamlit as st
from semantic_search import create_qdrant_collection,upload_vectors_to_qdrant_collection,semantic_search_qdrant
from keyword_search import keyword_search
from searchs_combined import reciprocal_rank_fusion

# Streamlit UI
st.header(":blue[Hybrid Search: _Semantic and Keyword Search Integration_]")

# Placeholder documents for demonstration
documents = [
    "Artificial Intelligence is the future of technology.",
    "Machine learning is a subset of artificial intelligence.",
    "Deep learning models can learn from large amounts of data.",
    "A dog is not feeling well.",
    "Natural Language Processing is used for understanding human language."
]

query = st.text_input("Enter your search query:")

if query:
    st.write("Performing Semantic and Keyword Search...")

    ######## Perform searches ######
    #Load Semantic search and its functions using with DB
    create_qdrant_collection()
    upload_vectors_to_qdrant_collection(documents)
    semantic_results, semantic_scores = semantic_search_qdrant(query) 

    #Load Keyword search
    keyword_results, keyword_scores = keyword_search(query, documents)

    # Display individual results
    st.write("**Semantic Search Results**")
    for i, result_doc in enumerate(semantic_results):
        st.write(f"Document {i + 1}: {result_doc} (Score: {semantic_scores[i]:.4f})")

    st.write("**Keyword Search Results**")
    for i, doc_id in enumerate(keyword_results):
        st.write(f"Document {doc_id + 1}: {documents[doc_id]} (Score: {keyword_scores[i]:.4f})")

    # Combine results using RRF
    combined_results = reciprocal_rank_fusion(semantic_results, keyword_results)
    
    st.write("**Combined Results** (Using Reciprocal Rank Fusion)")
    for i, doc_id in enumerate(combined_results):
        st.write(f"Document {doc_id + 1}: {documents[doc_id]}")
