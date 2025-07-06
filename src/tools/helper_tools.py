from src.tools.push_over_message_tool import push_over_message_tool
import os
from dotenv import load_dotenv

load_dotenv()

## pushover token
pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")

def record_user_details(email = "Not Provided", name="Name not provided", notes="not provided"):
    push_over_message_tool(f"Recording interest from {name} with email {email} and notes {notes}", pushover_user=pushover_user, pushover_token=pushover_token)
    return {"recorded": "ok"}

def record_unknown_question(question):
    push_over_message_tool(f"Recording {question} asked that I couldn't answer", pushover_user=pushover_user, pushover_token=pushover_token)
    return {"recorded": "ok"}

