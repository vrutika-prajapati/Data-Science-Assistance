from fastapi import FastAPI
from pydantic import BaseModel
from chatbot_assistant import ChatBot
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")
agent_id = os.getenv("MISTRAL_AGENT_ID")

if not api_key or not agent_id:
    raise ValueError("❌ API keys missing! Check your .env file.")

# Initialize chatbot
chatbot = ChatBot(api_key, agent_id)

app = FastAPI()

# Pydantic model for input
class Query(BaseModel):
    prompt: str

@app.post("/chat/")
async def chat(query: Query):
    response = chatbot.generate_response(query.prompt)
    return {"response": response}
