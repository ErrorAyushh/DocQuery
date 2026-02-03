import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="DocQuery", layout="centered")

st.title("📄 DocQuery – Chat with your PDF")

st.header("Upload a PDF")

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file and st.button("Upload & Index"):
    with st.spinner("Uploading and indexing..."):
        files = {"file": uploaded_file}
        res = requests.post(f"{BACKEND_URL}/upload", files=files)

    if res.status_code == 200:
        st.success("PDF indexed successfully!")
        st.json(res.json())
    else:
        st.error("Upload failed")

st.divider()

st.header("Ask a question")

question = st.text_input("Your question")

if question and st.button("Ask"):
    with st.spinner("Thinking..."):
        res = requests.post(
            f"{BACKEND_URL}/chat",
            json={"question": question},
        )

    if res.status_code == 200:
        data = res.json()
        st.subheader("Answer")
        st.write(data["answer"])

        with st.expander("Context used"):
            for i, chunk in enumerate(data["context_used"], 1):
                st.markdown(f"**Chunk {i}:** {chunk}")
    else:
        st.error("Chat failed")
