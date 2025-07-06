import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import List, Dict

from src.controller.chat_controller import ChatController

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## status api
@app.get("/")
def hello_world():
    return "Hello World"


class ChatRequest(BaseModel):
    message: str
    history: List[Dict[str, str]] = []

controller = ChatController()

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """
    Endpoint to handle chat messages. Expects a JSON body with 'message' and optional 'history'.
    Returns the assistant's response.
    """

    reply = controller.chat(request.message, request.history)
    return {"response": reply}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)