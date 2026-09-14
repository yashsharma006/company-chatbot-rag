from langchain_core.prompts import PromptTemplate

def get_prompt():

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a helpful company assistant.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}

Answer:
"""
    )

    return prompt