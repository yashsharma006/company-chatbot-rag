from src.loader import load_documents
from src.splitter import split_documents
from src.vector_store import create_vector_store
from src.chatbot import ask_question

def main():

    print("Creating Knowledge Base...")

    documents = load_documents()

    chunks = split_documents(documents)

    create_vector_store(chunks)

    print("\nKnowledge Base Ready")

    while True:

        question = input("\nAsk Question (type exit to quit): ")

        if question.lower() == "exit":
            break

        answer = ask_question(question)

        print("\nAnswer:")
        print(answer)


if name == "main":
    main()