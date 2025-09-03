from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/webhook")
async def receive_webhook(payload: dict):
    """
    This function receives WhatsApp messages from Openlyne
    """
    # Check if this is a new message
    if payload.get("event") == "messages.upsert":
        data = payload.get("data", {})
        print(f"📱 New message: {data}")
    
    # Add your response logic here
    # For example: send a reply, save to database, etc.

    return {"status": "received"}

if __name__ == "__main__":
    print("🚀 Starting openlyne webhook server...")
    print("🔗 Webhook URL: http://localhost:8000/webhook")
    uvicorn.run(app, host="0.0.0.0", port=8000)