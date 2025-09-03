from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/webhook")
async def evolution_webhook(payload: dict):
    # Log full payload for debugging (optional):
    event = payload.get("event")

    if event == "messages.upsert":
        data = payload.get("data", {})

        key = data.get("key", {})
        remote_jid = key.get("remoteJid")  # e.g. 254101886585@s.whatsapp.net
        from_me = key.get("fromMe")
        message_id = key.get("id")

        push_name = data.get("pushName")
        status = data.get("status")  # e.g. DELIVERY_ACK
        message_type = data.get("messageType")  # e.g. conversation
        message_ts = data.get("messageTimestamp")

        message = data.get("message", {})
        text = message.get("conversation") or ""

        # Compact summary log
        print(
            "Incoming message:",
            {
                "from": remote_jid,
                "name": push_name,
                "text": text,
                "type": message_type,
                "status": status,
                "id": message_id,
                "from_me": from_me,
                "ts": message_ts,
            },
        )

    return {"status": "received"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)