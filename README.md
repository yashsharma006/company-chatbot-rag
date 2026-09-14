
### 2. Company Knowledge Base Chatbot

```md
# Company Knowledge Base Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built with Python and Streamlit. The application allows users to upload company PDF documents, create a searchable knowledge base, and ask context-aware questions.

## Features

- Uploads and processes company PDF documents
- Extracts text from PDFs using PyPDFLoader
- Splits documents into overlapping chunks for improved context retrieval
- Generates semantic embeddings using Sentence Transformers
- Stores embeddings in a FAISS vector database
- Retrieves the most relevant document chunks using similarity search
- Uses Ollama and Llama 3.2 to generate context-based answers
- Uses a grounded prompt to ensure answers are based only on uploaded company documents
- Provides both Streamlit web application and command-line support

## Technologies Used

- Python
- Streamlit
- LangChain
- Ollama
- Llama 3.2
- FAISS
- Hugging Face Sentence Transformers
- PyPDF
- RAG

## Project Structure

```text
company_chatbotai_rag/
│
├── data/
│   └── Company PDF documents
│
├── db/
│   └── faiss_index/
│
├── src/
│   ├── loader.py
│   ├── splitter.py
│   ├── embedder.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── prompt.py
│   ├── llm.py
│   └── chatbot.py
│
├── app.py
├── main.py
└── requirenebts.txt

How It Works
1. The user uploads a company PDF through the Streamlit interface.
2. The application extracts document content using PyPDFLoader.
3. The text is divided into chunks with overlap to retain context between sections.
4. Each chunk is converted into vector embeddings using the all-MiniLM-L6-v2 embedding model.
5. The embeddings are stored locally in a FAISS vector database.
6. When the user asks a question, the system retrieves the top three relevant chunks.
7. The retrieved document context and question are sent to the Llama 3.2 model.
8. The chatbot returns an answer based only on the provided company document context.
