from llama_index.readers.file import PyMuPDFReader
from llama_index.core import VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.settings import Settings
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Set LLM and embedding models
Settings.llm = OpenAI(model="gpt-4", api_key=api_key)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small", api_key=api_key)

# Load PDF using correct reader
pdf_reader = PyMuPDFReader()
documents = pdf_reader.load(file_path="data/notion.pdf")

# Create vector index
index = VectorStoreIndex.from_documents(documents)

# Query
query_engine = index.as_query_engine()
response = query_engine.query("Explain this PDF in detail.")
print(response)
