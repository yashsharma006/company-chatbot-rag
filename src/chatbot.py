from src.retriever import retrieve_documents
from src.prompt import get_prompt
from src.llm import get_llm

def ask_question(question):

    documents = retrieve_documents(question)

    context = ""
    for doc in documents:
        context = context + doc.page_content + "\n\n"

    prompt = get_prompt()

    final_prompt = prompt.format(
        context=context,
        question=question
    )

    llm = get_llm()

    response = llm.invoke(final_prompt)

    return response.content