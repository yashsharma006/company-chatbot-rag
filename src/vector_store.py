from langchain_community.vectorstores import FAISS
from src.embedder import get_embedding_model

DB_PATH = "db/faiss_index"


def create_vector_store(chunks):
    embeddings = get_embedding_model()

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    vector_store.save_local(DB_PATH)


def load_vector_store():
    embeddings = get_embedding_model()

    vector_store = FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store