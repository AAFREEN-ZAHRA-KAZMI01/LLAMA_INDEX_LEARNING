# chat_engine.py
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.chat_engine import ContextChatEngine
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.schema import Document

from custom_prompt import SYSTEM_PROMPT  # No dot here

def build_chat_engine():
    # Dummy document to help initialize vector index
    dummy_doc = Document(text="This chatbot only answers questions related to Pakistan.")
    index = VectorStoreIndex.from_documents([dummy_doc])
    retriever = index.as_retriever()

    # Set LLM and Embeddings
    llm = OpenAI(model="gpt-3.5-turbo", temperature=0)
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

    # Register globally
    Settings.llm = llm
    Settings.embed_model = embed_model

    # Memory
    memory = ChatMemoryBuffer.from_defaults(token_limit=3000)

    # Chat Engine using ContextChatEngine
    chat_engine = ContextChatEngine.from_defaults(
        retriever=retriever,
        llm=llm,
        memory=memory,
        system_prompt=SYSTEM_PROMPT,
        verbose=True
    )

    return chat_engine
