# utils/rag_engine.py
import os 
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.settings import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai import OpenAI

def build_chat_engine_from_file(file_path):
    documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

    llm = OpenAI(temperature=0, model="gpt-3.5-turbo")
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

    # NEW WAY: Set LLM and embed_model globally using Settings
    Settings.llm = llm
    Settings.embed_model = embed_model

    index = VectorStoreIndex.from_documents(documents)
    return index.as_chat_engine(chat_mode="condense_question", verbose=True)
