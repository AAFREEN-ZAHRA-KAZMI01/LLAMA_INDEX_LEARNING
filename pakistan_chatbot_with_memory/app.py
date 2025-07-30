# app.py
import os

import streamlit as st
from chat_engine import build_chat_engine
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Pakistan Chatbot with Memory")

if "chat_engine" not in st.session_state:
    st.session_state.chat_engine = build_chat_engine()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🇵🇰 Pakistan Chatbot with Memory")

# Tabs
tab1, tab2 = st.tabs(["💬 Chat", "🕓 History"])

with tab1:
    user_input = st.text_input("Ask a question related to Pakistan:", key="input")

    if st.button("Ask"):
        if user_input:
            response = st.session_state.chat_engine.chat(user_input)
            st.session_state.chat_history.append({"user": user_input, "bot": response.response})
            st.markdown(f"**You:** {user_input}")
            st.markdown(f"**Bot:** {response.response}")

with tab2:
    st.subheader("🕓 Past Questions & Responses")
    for item in st.session_state.chat_history:
        st.markdown(f"**You:** {item['user']}")
        st.markdown(f"**Bot:** {item['bot']}")
        st.markdown("---")
