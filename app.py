from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://rodrigovcoding.github.io",  # Permite GH Pages
        "http://127.0.0.1:5500"              # Se quiser testar local
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(request: PromptRequest):
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(request.prompt)
    return {"response": response.text}