import os
import requests

def send_text(phone, text):
    response = requests.post("https://api.openlyne.com/v1/sendText", 
    headers={"x-api-key": "OPENLYNE_API_KEY"},
    json={
        "number": phone,
        "message": text,
        "project_id": "PROJECT_ID"
    })

    print("Message sent!")
    return response.json()

# Example use
send_text("256XXXXXXXXXX", "Hello from Openlyne!")