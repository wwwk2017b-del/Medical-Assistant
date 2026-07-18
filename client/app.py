import streamlit as st
from components.upload import render_uploader
from components.history_download import render_history_download
from components.chatUI import render_chat

st.set_page_config(page_title="NeuroDoc", page_icon="⚡", layout="wide")

# High-End 3D Cyberpunk Anime CSS Injection
st.markdown("""
<style>
    /* Import Sci-Fi fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@500;700&display=swap');

    /* Global styling */
    html, body, [class*="css"] {
        font-family: 'Rajdhani', sans-serif;
    }

    /* Cyberpunk Deep Dark Background */
    .stApp {
        background-color: #0A0A0F;
        background-image: 
            radial-gradient(circle at 15% 50%, rgba(255, 0, 255, 0.08), transparent 25%),
            radial-gradient(circle at 85% 30%, rgba(0, 255, 255, 0.1), transparent 25%);
        color: #e0e0ff;
    }

    /* 3D Glass Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(10, 10, 15, 0.6) !important;
        backdrop-filter: blur(15px) !important;
        border-right: 2px solid rgba(0, 255, 255, 0.3) !important;
        box-shadow: 5px 0 25px rgba(0, 255, 255, 0.1);
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Chat Input Container - Glowing Focus */
    .stChatInputContainer {
        background: rgba(20, 20, 25, 0.8) !important;
        border-radius: 12px !important;
        border: 2px solid rgba(255, 0, 255, 0.4) !important;
        box-shadow: 0 0 15px rgba(255, 0, 255, 0.2), inset 0 0 10px rgba(255, 0, 255, 0.1) !important;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    .stChatInputContainer:focus-within {
        border-color: #00ffff !important;
        box-shadow: 0 0 25px rgba(0, 255, 255, 0.5), inset 0 0 15px rgba(0, 255, 255, 0.2) !important;
        transform: scale(1.01);
    }
    
    /* 3D Floating Buttons with Snappy Hover */
    .stButton>button {
        background: linear-gradient(45deg, #ff00ff, #00ffff);
        color: #ffffff;
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        letter-spacing: 1px;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        box-shadow: 0 6px 0 #8b008b, 0 10px 20px rgba(255, 0, 255, 0.4);
        transition: all 0.15s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-transform: uppercase;
    }
    .stButton>button:hover {
        transform: translateY(-4px) scale(1.05);
        box-shadow: 0 10px 0 #8b008b, 0 15px 30px rgba(0, 255, 255, 0.6);
        color: white;
    }
    .stButton>button:active {
        transform: translateY(4px);
        box-shadow: 0 2px 0 #8b008b, 0 5px 10px rgba(255, 0, 255, 0.4);
    }

    /* Animated Cyberpunk Header */
    h1 {
        font-family: 'Orbitron', sans-serif;
        background: linear-gradient(90deg, #00ffff, #ff00ff, #39ff14);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
        animation: shine 3s linear infinite;
    }
    @keyframes shine {
        to { background-position: 200% center; }
    }
    
    /* 3D Glass Chat Messages */
    [data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(0, 255, 255, 0.2);
        border-radius: 12px;
        box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.5), inset 1px 1px 0 rgba(255,255,255,0.05);
        margin-bottom: 1rem;
        backdrop-filter: blur(5px);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    [data-testid="stChatMessage"]:hover {
        transform: perspective(1000px) rotateX(2deg) rotateY(-2deg) scale(1.01);
        border-color: rgba(255, 0, 255, 0.4);
        box-shadow: 8px 8px 25px rgba(255, 0, 255, 0.15), inset 1px 1px 0 rgba(255,255,255,0.1);
    }
</style>
""", unsafe_allow_html=True)

st.title("⚡ NeuroDoc")

render_uploader()
render_chat()
render_history_download()