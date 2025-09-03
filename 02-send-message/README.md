# Tutorial 02: Send a Text Message

This guide shows three simple ways to send a WhatsApp text message using the Openlyne API:
- curl (no code, just your terminal)
- Python
- JavaScript (Node.js)

If you finished Tutorial 01, you’re ready. If not, start there first.

## Prerequisites

- Openlyne API key and Project ID
- A `.env` file in the repo root:
  
  ```env
  OPENLYNE_API_KEY=your_api_key_here
  PROJECT_ID=your_project_id_here
  ```
- A WhatsApp number in E.164 format (example placeholder: 256XXXXXXXXXX)

## ⚠️ Important: Message Consent & Compliance

**Example Numbers Only**: The phone number `256XXXXXXXXXX` shown in examples is **NOT REAL**. Always replace with actual test numbers.

**User Consent Required**: Only send messages to users who have explicitly consented to receive them. Unsolicited messages violate WhatsApp policies and may be illegal.

**Rate Limits**: Respect API limits to avoid account suspension. Start with small test volumes.

**Data Protection**: Ensure compliance with local privacy laws when handling user data and phone numbers.

---

## 1) Send with curl

Replace the placeholders with your real values:

```bash
curl -X POST https://api.openlyne.com/v1/sendText \
  -H "x-api-key: $OPENLYNE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "number": "256XXXXXXXXXX",
    "message": "Hello from Openlyne!",
    "project_id": "'$PROJECT_ID'"
  }'
```

Expected response (example):

```json
{
  "success": true,
  "data": { /* message details */ },
  "message": "sent"
}
```

---

## 2) Send with Python

Install once (if not already):

```bash
pip install requests python-dotenv
```

Run the example file:

```bash
python send.py
```

---

## 3) Send with JavaScript (Node.js)

Install once (if not already):

```bash
npm init -y
npm install axios dotenv
```

Run the example file:

```bash
node send.js
```

---

## Tips

- Use E.164 phone format (no leading + in this example): 256XXXXXXXXXX
- Keep `.env` out of version control
- If you get an error, print the response body to see details

## Next

- Try dynamic messages (variables from your app)
- Send to multiple recipients (loop over a list)
- Explore other endpoints in the docs