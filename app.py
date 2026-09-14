import os
import streamlit as st

from src.loader import load_documents
from src.splitter import split_documents
from src.vector_store import create_vector_store
from src.chatbot import ask_question


st.set_page_config(
    page_title="Company Knowledge Base Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Company Knowledge Base Chatbot")

uploaded_file = st.file_uploader("Upload a PDF",type=["pdf"])

if uploaded_file:

    os.makedirs("data", exist_ok=True)

    pdf_path = os.path.join("data",uploaded_file.name)

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF Uploaded Successfully")

    if st.button("Create Knowledge Base"):

        with st.spinner("Creating Vector Database..."):

            documents = load_documents(pdf_path)

            chunks = split_documents(documents)

            create_vector_store(chunks)

        st.success("Knowledge Base Created Successfully")

st.divider()

question = st.text_input("Ask a Question")

if st.button("Ask"):

    with st.spinner("Searching..."):

        answer = ask_question(question)

    st.write(answer)