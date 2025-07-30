from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.settings import Settings
from dotenv import load_dotenv
import os

# ✅ Load environment variables from .env file
load_dotenv()

# 🗝️ Get the API key from .env
api_key = os.getenv("OPENAI_API_KEY")

# 🧠 Set LLM and Embeddings
Settings.llm = OpenAI(model="gpt-4", api_key=api_key)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small", api_key=api_key)

# 📁 Load ONLY `.txt` files from 'data' folder
documents = SimpleDirectoryReader(
    input_dir="data",
    required_exts=[".txt"]  # 🧽 Filter only .txt files, ignore .pdf
).load_data()

# 🔎 Create vector index
index = VectorStoreIndex.from_documents(documents)

# ❓ Query
query_engine = index.as_query_engine()
response = query_engine.query("Explain the content of this document.")
print(response)
