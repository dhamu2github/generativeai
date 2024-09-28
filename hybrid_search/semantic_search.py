# semantic_search.py

import qdrant_client
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer

# Load the pre-trained model for dense vector generation
#model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # You can use a different model here
model = SentenceTransformer("all-MiniLM-L6-v2")

# Qdrant Client Initialization
client = qdrant_client.QdrantClient(host="localhost", port=6333)

# Qdrant Client Initialization
collection_name = "hybrid_search_collection"

# Function to check if a collection exists
def collection_exists(client, collection_name):
    try:
        collections = client.get_collections().collections
        collection_names = [collection.name for collection in collections]
        return collection_name in collection_names # This return True
    except Exception as e:
        print(f"Error occurred while checking for collection: {e}")
        return False
    
# Function to create collection (db table)
# Vector size from the model
# setting up the COSINE similarity    
def create_qdrant_collection():
    #checking collection exisits or not
    if not collection_exists(client, collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(
                size=model.get_sentence_embedding_dimension(),  # Vector size is defined by used model
                distance=models.Distance.COSINE,
            ),
        )

def upload_vectors_to_qdrant_collection(documents):
    vectors = [model.encode(doc).tolist() for doc in documents]
    payload = [{"document_text": doc} for doc in documents]
    
    client.upload_collection(
        collection_name=collection_name,
        vectors=vectors,
        payload=payload,
        ids=list(range(len(documents)))
    )

def semantic_search_qdrant(query, top_k=5):
    query_vector = model.encode([query])[0].tolist()
    search_result = client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=top_k
    )
    return search_result

#Following code for unit testing
if __name__ == "__main__":

    #invoke create collection method
    create_qdrant_collection()

    #sample data for testing
    documents = ["Artificial Intelligence","Machine learning","Neural Network","A dog is not feeling well","Generative AI"]
    upload_vectors_to_qdrant_collection(documents)

    #sample query
    query = "veterinary"
    
    #call sematic search function
    semantic_results = semantic_search_qdrant(query) # with DB


    # Further unpack from the main list
    doc_ids = [hit.id for hit in semantic_results]
    doc_texts = [hit.payload["document_text"] for hit in semantic_results]
    scores = [hit.score for hit in semantic_results]

    for i, doc in enumerate(semantic_results):
        print(f"Document {doc_ids[i] + 1}: {doc_texts[i]} (Score: {scores[i]:.4f})")