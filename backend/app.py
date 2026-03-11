from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from rag.loader import load_documents
from rag.splitter import split_documents
from rag.vectordb import create_vector_db
from api.chat import router as chat_router

app = FastAPI()

DB_PATH = "chroma_db"

origins = [
    "https://aau-chatbot-liart.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    if not os.path.exists(DB_PATH):
        print("Creating embeddings...")
        documents = load_documents()
        chunks = split_documents(documents)
        create_vector_db(chunks)
        print("Embeddings created!")
    else:
        print("Vector DB already exists.")

app.include_router(chat_router, prefix="/api")