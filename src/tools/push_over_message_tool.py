import requests

pushover_url = "https://api.pushover.net/1/messages.json"

def push_over_message_tool(message, pushover_user, pushover_token):
    print(f"Push: {message}")
    payload = {"user": pushover_user, "token": pushover_token, "message": message}
    requests.post(pushover_url, data=payload)