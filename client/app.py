import os
import streamlit as st
from components.upload import render_uploader
from components.history_download import render_history_download
from components.chatUI import render_chat

st.set_page_config(page_title="NeuroDoc: Thunder Form", page_icon="⚡", layout="wide")

# Zenitsu Thunder Breathing CSS Injection
st.markdown("""
<style>
    /* Import Sci-Fi and Anime fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@500;700&display=swap');

    /* Global styling */
    html, body, [class*="css"] {
        font-family: 'Rajdhani', sans-serif;
    }

    /* Thunder Breathing Deep Dark Background */
    .stApp {
        background-color: #050505;
        background-image: 
            radial-gradient(circle at 50% -20%, rgba(255, 215, 0, 0.15), transparent 40%),
            radial-gradient(circle at 10% 80%, rgba(255, 255, 255, 0.05), transparent 30%);
        color: #e0e0ff;
    }

    /* 3D Glass Sidebar struck by lightning */
    [data-testid="stSidebar"] {
        background: rgba(5, 5, 5, 0.7) !important;
        backdrop-filter: blur(15px) !important;
        border-right: 2px solid rgba(255, 215, 0, 0.4) !important;
        box-shadow: 8px 0 30px rgba(255, 215, 0, 0.15);
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Chat Input Container - Electric Focus */
    .stChatInputContainer {
        background: rgba(15, 15, 15, 0.9) !important;
        border-radius: 12px !important;
        border: 2px solid rgba(255, 215, 0, 0.3) !important;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.1), inset 0 0 10px rgba(255, 215, 0, 0.05) !important;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    .stChatInputContainer:focus-within {
        border-color: #FFD700 !important;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.6), inset 0 0 15px rgba(255, 215, 0, 0.3) !important;
        transform: scale(1.02);
    }
    
    /* Thunder Form Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #FFD700, #FFA500);
        color: #000000;
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        letter-spacing: 1px;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        box-shadow: 0 6px 0 #B8860B, 0 10px 20px rgba(255, 215, 0, 0.4);
        transition: all 0.15s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-transform: uppercase;
    }
    .stButton>button:hover {
        transform: translateY(-4px) scale(1.05);
        box-shadow: 0 10px 0 #B8860B, 0 15px 35px rgba(255, 215, 0, 0.7);
        color: #000000;
    }
    .stButton>button:active {
        transform: translateY(4px);
        box-shadow: 0 2px 0 #B8860B, 0 5px 10px rgba(255, 215, 0, 0.4);
    }

    /* Animated Thunder Header */
    h1 {
        font-family: 'Orbitron', sans-serif;
        background: linear-gradient(90deg, #FFD700, #FFFFFF, #FFD700);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 0 0 25px rgba(255, 215, 0, 0.5);
        animation: lightning 3s linear infinite;
    }
    @keyframes lightning {
        to { background-position: 200% center; }
    }
    
    /* 3D Glass Chat Messages - AI & User */
    [data-testid="stChatMessage"] {
        border-radius: 12px;
        margin-bottom: 1rem;
        backdrop-filter: blur(5px);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    /* User Chat Bubble (Dark with yellow border) */
    [data-testid="stChatMessage"][data-testid*="user"] {
        background: rgba(15, 15, 15, 0.8);
        border: 1px solid rgba(255, 215, 0, 0.5);
        box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.8);
    }

    /* AI Chat Bubble (Glowing Glass) */
    [data-testid="stChatMessage"][data-testid*="assistant"] {
        background: rgba(255, 215, 0, 0.05);
        border: 1px solid rgba(255, 215, 0, 0.2);
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.1), inset 1px 1px 0 rgba(255, 255, 255, 0.1);
    }
    
    [data-testid="stChatMessage"]:hover {
        transform: perspective(1000px) rotateX(2deg) rotateY(-2deg) scale(1.01);
        border-color: rgba(255, 215, 0, 0.8);
        box-shadow: 8px 8px 30px rgba(255, 215, 0, 0.2), inset 1px 1px 0 rgba(255, 255, 255, 0.2);
    }
    
    /* Zenitsu Image Styling */
    [data-testid="stImage"] img {
        border-radius: 12px;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.4);
        border: 2px solid #FFD700;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚡ NeuroDoc: Thunder Form")

# Inject Zenitsu Image in sidebar securely
if os.path.exists("zenitsu.jpg"):
    st.sidebar.image("zenitsu.jpg", use_column_width=True)
elif os.path.exists("client/zenitsu.jpg"):
    st.sidebar.image("client/zenitsu.jpg", use_column_width=True)
else:
    st.sidebar.warning("⚡ Zenitsu image not found. Please add 'zenitsu.jpg' to the client folder and push to GitHub.")

render_uploader()
render_chat()
render_history_download()