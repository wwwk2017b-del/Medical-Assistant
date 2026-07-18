# 🧠 NeuroDoc: Universal Document Assistant

![NeuroDoc UI](https://img.shields.io/badge/UI-Cyberpunk_3D-0A0A0F?style=for-the-badge&color=ff00ff)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97_Hugging_Face-FFD21E?style=for-the-badge&logoColor=black)
![Pinecone](https://img.shields.io/badge/Pinecone-000000?style=for-the-badge)

NeuroDoc is a high-performance, Full-Stack AI application that allows users to upload any PDF document and instantly extract knowledge from it using a conversational AI interface. Built with a highly advanced 3D Cyberpunk aesthetic, it leverages a robust **RAG (Retrieval-Augmented Generation)** architecture to deliver lightning-fast, accurate responses.

## 🚀 Tech Stack & Architecture

This project is built using modern AI and web frameworks to ensure scalability, speed, and accuracy:

*   **Frontend (Streamlit)**: A custom-injected CSS glassmorphism UI featuring responsive 3D elements, neon accents, and snappy animations.
*   **Backend API (FastAPI)**: A lightweight, high-performance REST API hosted on Render that handles file processing and AI orchestration.
*   **AI Brain (Groq + Llama 3)**: Utilizing `Llama-3.3-70b-versatile` via the Groq API for near-instantaneous language generation.
*   **Embeddings (Hugging Face + Pinecone)**: We use the `multilingual-e5-large` Hugging Face model. To overcome local memory limits on free-tier servers, we offload the heavy embedding computations directly to **Pinecone's Serverless Inference API**.
*   **Vector Database (Pinecone)**: Stores the high-dimensional document vectors for rapid semantic search.
*   **Orchestration (LangChain)**: The glue that binds the RAG pipeline together, handling document splitting, vector retrieval, and prompt injection.

## 🧠 How the RAG Pipeline Works

This application demonstrates a textbook implementation of Retrieval-Augmented Generation:

1.  **Ingestion**: A user uploads a PDF. The FastAPI backend uses LangChain's `PyPDFLoader` to extract the text and `RecursiveCharacterTextSplitter` to chop it into small, manageable chunks.
2.  **Embedding**: These chunks are sent in batches to the Pinecone Inference API (running Hugging Face's `multilingual-e5-large`), converting the text into mathematical vectors.
3.  **Storage**: The vectors and their original text (metadata) are upserted into a Pinecone Serverless Index.
4.  **Retrieval (The 'R' in RAG)**: When a user asks a question, the question is converted into a vector, and Pinecone performs a similarity search to "retrieve" the most relevant paragraphs from the PDF.
5.  **Generation (The 'G' in RAG)**: The retrieved paragraphs are injected into a strict prompt template alongside the user's question, and sent to Groq's Llama-3 model to "generate" a precise, context-aware answer.

## 💡 Overcoming Cloud Constraints (The Engineering Challenge)

When deploying to free-tier cloud servers (like Render's 512MB RAM tier), processing large PDFs locally caused immediate `Out Of Memory (OOM)` crashes and `100-second Timeout` limits. 

**The Solution:** 
Instead of running local PyTorch models, the architecture was optimized to rely entirely on external serverless APIs. By implementing **chunk-batching** and utilizing **Pinecone's Inference API** for embeddings instead of local computation, the backend can now process massive documents in seconds with virtually zero memory overhead.

## 💻 Local Setup & Installation

1. **Clone the repository**
```bash
git clone https://github.com/wwwk2017b-del/Medical-Assistant.git
cd Medical-Assistant
```

2. **Backend Setup (FastAPI)**
```bash
cd server
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```
Create a `.env` file in the `server` folder with your API keys:
```
GROQ_API_KEY=your_key_here
PINECONE_API_KEY=your_key_here
```
Start the backend server:
```bash
uvicorn main:app --reload
```

3. **Frontend Setup (Streamlit)**
Open a new terminal and run:
```bash
cd client
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
