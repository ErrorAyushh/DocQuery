from langchain_groq import ChatGroq
from app.rag.retriever import retrieve_chunks
from app.rag.prompt import SYSTEM_PROMPT
from app.core.config import settings


def answer_question(question: str):
    if not settings.GROQ_API_KEY:
        raise RuntimeError("GROQ_API_KEY not loaded")

    chunks = retrieve_chunks(question)

    if not chunks:
        return {
            "answer": "I don't know based on the provided documents.",
            "context_used": []
        }

    context_blocks = []
    for src in chunks:
        context_blocks.append(
        f"(page {src['page']}) {src['text']}"
    )

    context = "\n\n".join(context_blocks)

    llm = ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model="llama-3.1-8b-instant",
        temperature=0,
    )

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": f"""
Context:
{context}

Question:
{question}
""",
        },
    ]

    response = llm.invoke(messages)

    return {
    "answer": response.content,
    "sources": chunks
}
