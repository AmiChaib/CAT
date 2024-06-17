from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from langchain_openai import ChatOpenAI

from container import container
# This must be set in a .env file containing the API key:
# OPENAI_API_KEY="<<key>>"
from config import OPENAI_API_KEY 
from classes import UserInput

from prompt_templates import ANALYSIS_TEMPLATE

# App
# ----------------------
app = FastAPI()

# CORS Setup
# ----------------------
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8080/input",
    "http://localhost:8080/result",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoints
# ----------------------
@app.get("/") # Just for testing
def read_root():
    return {"CAT": "Version 1.0"}

@app.post("/analyse")
async def create_analysis(userInput: UserInput):
    input_text = userInput.input_text
    input_categories = userInput.input_categories
    template = ANALYSIS_TEMPLATE
    model = ChatOpenAI(temperature=0.3)
    results = container.client.detect_categories(model, template, input_categories, input_text)
    return results

# @app.post("/test") # Just for testing
# async def test(userInput: UserInput):
#     return userInput