# 📄 DocQuery – Chat with Your PDFs using RAG

DocQuery is a **Retrieval-Augmented Generation (RAG)** application that allows users to **upload PDF documents and ask natural-language questions**, receiving **accurate, context-aware answers with source citations**.

This project demonstrates a **production-style RAG pipeline**, combining semantic search with LLM reasoning to ensure answers are grounded in the original documents.

---

## ✨ Key Features

- 📂 Upload PDFs and extract text automatically
- ✂️ Intelligent document chunking
- 🧠 Semantic search using vector embeddings
- 🔎 Context-aware question answering (RAG)
- 📌 Page-level source citations
- ⚡ FastAPI backend
- 🎨 Streamlit frontend
- 🧱 Vector database powered by Qdrant
- 🤖 LLM inference using Groq

---

## 🧠 How It Works (RAG Pipeline)

1. **PDF Upload**
   - User uploads a PDF via UI or API
   - Text is extracted page-wise

2. **Chunking**
   - Text is split into overlapping chunks for better semantic retrieval

3. **Embeddings**
   - Each chunk is converted into a dense vector using SentenceTransformers

4. **Vector Storage**
   - Embeddings are stored in Qdrant for fast similarity search

5. **Question Answering**
   - User query is embedded
   - Relevant chunks are retrieved from Qdrant
   - Retrieved context is passed to the LLM
   - LLM generates an answer with citations

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- LangChain
- SentenceTransformers
- Qdrant
- Groq LLM API

### Frontend
- Streamlit

### Infrastructure
- Docker
- REST APIs
- Environment-based configuration

---

## 📂 Project Structure

```text
docquery/
│
├── backend/
│   ├── app/
│   │   ├── api/        # Upload & Chat endpoints
│   │   ├── rag/        # Loader, splitter, embeddings, retriever, QA
│   │   ├── core/       # Config & environment handling
│   │   └── main.py
│   └── .env.example
│
├── frontend/
│   └── ui.py           # Streamlit UI
│
├── docker-compose.yml
├── .gitignore
└── README.md
