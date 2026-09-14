from src.vector_store import load_vector_store

def retrieve_documents(query):

    vector_store = load_vector_store()

    documents = vector_store.similarity_search(
        query=query,
        k=3
    )

    return documents