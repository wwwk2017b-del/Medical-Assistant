import os
import time
from pathlib import Path

from dotenv import load_dotenv
from tqdm.auto import tqdm

from pinecone import Pinecone, ServerlessSpec

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

PINECONE_ENV = "us-east-1"
PINECONE_INDEX_NAME = "medicalindex2"

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

UPLOAD_DIR = "./uploaded_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
spec = ServerlessSpec(
    cloud="aws",
    region=PINECONE_ENV
)

existing_indexes = [i["name"] for i in pc.list_indexes()]

if PINECONE_INDEX_NAME not in existing_indexes:
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=384,
        metric="dotproduct",
        spec=spec
    )

    while not pc.describe_index(PINECONE_INDEX_NAME).status["ready"]:
        time.sleep(1)

index = pc.Index(PINECONE_INDEX_NAME)


def load_vectorstore(uploaded_files):
    embed_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    file_paths = []

    for file in uploaded_files:
        save_path = Path(UPLOAD_DIR) / file.filename

        with open(save_path, "wb") as f:
            f.write(file.file.read())

        file_paths.append(str(save_path))

    for file_path in file_paths:
        loader = PyPDFLoader(file_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=30
        )

        chunks = splitter.split_documents(documents)

        texts = [chunk.page_content for chunk in chunks]
        metadatas = [{**chunk.metadata, "text": chunk.page_content} for chunk in chunks]
        ids = [f"{Path(file_path).stem}-{i}" for i in range(len(chunks))]

        print(f"Total chunks to process: {len(texts)}")
        batch_size = 100
        
        for i in range(0, len(texts), batch_size):
            batch_texts = texts[i:i+batch_size]
            batch_ids = ids[i:i+batch_size]
            batch_metadatas = metadatas[i:i+batch_size]
            
            print(f"Embedding and uploading batch {i//batch_size + 1}...")
            
            # Embed in batches to avoid Google API limits
            batch_embeddings = embed_model.embed_documents(batch_texts)
            
            # Upsert in batches to avoid Pinecone payload limits
            index.upsert(
                vectors=list(zip(batch_ids, batch_embeddings, batch_metadatas))
            )

        print(f"Upload complete for {file_path}")