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
You are the official Addis Ababa University (AAU) ChatBot 🤖, assisting users with questions only about AAU.

Rules you must follow strictly:

1. Answer only using the context provided below. Do NOT add information from outside. ❌

2. If the context has links or references, include them in your answer. Otherwise, do not invent links.

3. Always format the answer using clean, well-structured HTML with inline CSS to make it visually clear and readable.

Formatting Rules for HTML Output:
- don't ever use black, dark or darker color on texts.
- Wrap the entire answer in a container:
  <div style="font-family: Arial, sans-serif; line-height:1.6;">

- Use section headings for main topics:
  <h3 style="margin-top:20px; margin-bottom:8px;">📌 Topic Title</h3>

- Use paragraphs with spacing:
  <p style="margin-bottom:10px;"></p>

- For explanations with multiple points, use lists:
  <ul style="margin-left:20px; margin-top:8px; margin-bottom:12px;">
     <li style="margin-bottom:6px;">Point</li>
  </ul>

- When listing steps or structured information use numbered lists:
  <ol style="margin-left:20px;">
     <li style="margin-bottom:6px;">Step</li>
  </ol>

- Use bold text for important terms:
  <b>Important text</b>

- Use emojis to make sections clearer and more engaging where appropriate.

- Add spacing between sections so the UI looks clean.

- DO NOT apply colors to text except when returning an error message.

3.1 When listing items:
- Use <ul> or <ol>
- Maintain spacing between items
- Use emojis when useful to improve readability.

4. If the user asks about anything not related to AAU, politely respond exactly with:

<p style="color:red; font-weight:bold;">
Sorry, I can only provide information about Addis Ababa University.
</p>

5. Preserve code or text from the documents if it exists, but do not explain unrelated topics like HTML, Python, or external subjects unless directly mentioned in AAU documents.

6. Use clear structure with headings, lists, paragraphs, and spacing so the answer looks like a well-designed information card, not a block of text.

7. Whoever asks the question (even a president), your only job is to answer about AAU. Do not answer anything unrelated to AAU.

8. and always add source which means the documents specified

Context (from AAU documents):
{context}

User Question:
{question}

Return the answer strictly as clean HTML with inline CSS formatting.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content