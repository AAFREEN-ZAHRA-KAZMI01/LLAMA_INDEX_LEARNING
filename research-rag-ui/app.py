# app.py
import streamlit as st
from utils.rag_engine import build_chat_engine_from_file
import tempfile
import os

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")

st.title("📄 Document Q&A Chatbot")
st.markdown("Upload a `.pdf` or `.txt` file, and ask any question about it.")

# Upload section
uploaded_file = st.file_uploader("Upload your document", type=["pdf", "txt"])

# Session to hold chatbot engine
if "chat_engine" not in st.session_state:
    st.session_state.chat_engine = None

# Process uploaded file
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    st.success("📚 File uploaded and indexed successfully!")

    st.session_state.chat_engine = build_chat_engine_from_file(tmp_file_path)
    os.remove(tmp_file_path)

# Chat section
if st.session_state.chat_engine:
    question = st.text_input("💬 Ask a question about the document:")
    if question:
        response = st.session_state.chat_engine.chat(question)
        st.write("🤖", response.response)
