#!/usr/bin/env python3
"""
Tutorial 01: Getting Started - Python Version
Send your first WhatsApp message using the Openlyne API
"""

import os
import requests
from dotenv import load_dotenv

def main():
    load_dotenv()
    api_key = os.getenv('OPENLYNE_API_KEY')
    project_id = os.getenv('PROJECT_ID')
    url = "https://api.openlyne.com/v1/sendMessage"
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "number": "254101886585", # Replace with the recipient's phone number in international format
        "message": "Hello from my first WhatsApp bot!",
        "project_id": project_id
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.json())

if __name__ == "__main__":
    main()