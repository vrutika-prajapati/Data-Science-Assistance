import os
import streamlit as st
import re
from dotenv import load_dotenv
from chatbot_assistant import ChatBot

# === Load credentials ===
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")
agent_id = os.getenv("MISTRAL_AGENT_ID")

if not api_key or not agent_id:
    st.error("❌ API keys missing! Check your .env file.")
    st.stop()

chatbot = ChatBot(api_key, agent_id)

st.set_page_config(page_title="DS Chatbot", layout="wide")
st.title("💬 Data Science Chat Assistant")

# === Session State Initialization ===
if 'history' not in st.session_state:
    st.session_state.history = []
if 'code_response' not in st.session_state:
    st.session_state.code_response = None
if 'code_filename' not in st.session_state:
    st.session_state.code_filename = ""

CODES_DIR = "codes"
os.makedirs(CODES_DIR, exist_ok=True)

# === Intent Detection ===
def is_data_science_query(text):
    keywords = [
        "pandas", "dataframe", "matplotlib", "seaborn", "sklearn",
        "regression", "classification", "model", "data analysis",
        "plot", "train", "predict", "EDA", "xgboost", "numpy"
    ]
    return any(word in text.lower() for word in keywords)

def extract_code_blocks(text):
    return re.findall(r"```(?:python)?(.*?)```", text, re.DOTALL)

# === Chat Bubble HTML Style ===
def chat_bubble(role, content):
    bubble_color = "#DCF8C6" if role == "user" else "#F1F0F0"
    align = "right" if role == "user" else "left"
    name = "You" if role == "user" else "Assistant"
    return f"""
    <div style="display: flex; justify-content: {align}; margin: 10px 0;">
        <div style="
            padding: 10px 15px;
            border-radius: 15px;
            max-width: 70%;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        ">
            <strong>{name}:</strong><br>{content}
        </div>
    </div>
    """

# === Display Chat History with Bubbles ===
for msg in st.session_state.history:
    st.markdown(chat_bubble(msg["role"], msg["content"]), unsafe_allow_html=True)

# === Chat Input ===
user_prompt = st.chat_input("Type your message here...")

if user_prompt:
    st.session_state.history.append({"role": "user", "content": user_prompt})
    response = chatbot.generate_response(user_prompt)
    st.session_state.history.append({"role": "assistant", "content": response})

    st.session_state.code_response = None

    if is_data_science_query(user_prompt):
        code_blocks = extract_code_blocks(response)
        if code_blocks:
            st.session_state.code_response = code_blocks[0].strip()

    st.rerun()

# === Show Latest Code Response (if any) ===
if st.session_state.history and st.session_state.history[-1]["role"] == "assistant":
    if st.session_state.code_response:
        st.code(st.session_state.code_response, language='python')

        with st.expander("💾 Save this code?"):
            filename = st.text_input("Enter filename (no .py):", value=st.session_state.code_filename or "script1")
            if st.button("✅ Save Code"):
                safe_name = "_".join(filename.strip().split())
                filepath = os.path.join(CODES_DIR, f"{safe_name}.py")
                with open(filepath, "w") as f:
                    f.write(st.session_state.code_response)
                st.success(f"Code saved to `{filepath}`")
                st.session_state.code_filename = safe_name

# === Reset Option ===
if st.button("🔄 Reset Chat"):
    st.session_state.history = []
    st.session_state.code_response = None
    st.session_state.code_filename = ""
    st.rerun()
