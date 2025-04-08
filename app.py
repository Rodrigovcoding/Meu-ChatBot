
# Importa o framework FastAPI para criar APIs de forma rápida e eficiente.
from fastapi import FastAPI

# Importa o middleware CORS para permitir requisições de origens diferentes (Cross-Origin Resource Sharing).
from fastapi.middleware.cors import CORSMiddleware

# Importa a biblioteca Google Generative AI para interagir com modelos generativos da Google.
import google.generativeai as genai

# Importa o módulo `os` para acessar variáveis de ambiente do sistema.
import os

# Importa a função `load_dotenv` para carregar variáveis de ambiente de um arquivo `.env`.
from dotenv import load_dotenv

# Importa a classe `BaseModel` do Pydantic para validação de dados e criação de modelos.
from pydantic import BaseModel

# Carrega as variáveis de ambiente do arquivo `.env` para o ambiente do sistema.
load_dotenv()

# Obtém a chave de API do Google Generative AI a partir das variáveis de ambiente.
GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")

# Configura a biblioteca Google Generative AI com a chave de API obtida.
genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

# Cria uma instância do aplicativo FastAPI.
app = FastAPI()

# Adiciona o middleware CORS ao aplicativo para permitir requisições de origens específicas.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://rodrigovcoding.github.io",  # Permite requisições do GitHub Pages.
        "http://127.0.0.1:5500"              # Permite requisições locais para testes.
    ],
    allow_credentials=True,  # Permite o envio de cookies e credenciais.
    allow_methods=["*"],     # Permite todos os métodos HTTP (GET, POST, etc.).
    allow_headers=["*"],     # Permite todos os cabeçalhos HTTP.
)

# Define um modelo de dados chamado `PromptRequest` para validar o corpo das requisições.
class PromptRequest(BaseModel):
    prompt: str  # O modelo espera um campo `prompt` do tipo string.

# Define uma rota POST no endpoint `/chat`.
@app.post("/chat")
async def chat(request: PromptRequest):
    # Cria uma instância do modelo generativo da Google com o nome especificado.
    model = genai.GenerativeModel("models/gemini-2.5-pro-exp-03-25")
    
    # Gera conteúdo com base no `prompt` enviado na requisição.
    response = model.generate_content(request.prompt)
    
    # Retorna a resposta gerada como um dicionário JSON.
    return {"response": response.text}