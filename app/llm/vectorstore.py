import os
from langchain.vectorstores import FAISS
from app.llm.embeddings import embeddings
from app.config import Config

vectorstore = FAISS.load_local(Config.VECTOR_DB_PATH, embeddings)
