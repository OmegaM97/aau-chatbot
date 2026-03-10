import os
from dotenv import load_dotenv
from groq import Groq
from rag.retriever import get_retriever

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is not set in your environment or .env file.")

client = Groq(api_key=api_key)


def ask_question(question: str) -> str:
    """
    Ask a question to the RAG system and get a response from Groq.
    """
    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an assistant answering questions about Addis Ababa University.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content