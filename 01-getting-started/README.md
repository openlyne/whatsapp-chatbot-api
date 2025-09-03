
# WhatsApp Chatbot API: Quickstart

Welcome! This guide helps you send your first WhatsApp message using the Openlyne API. Follow these steps to get started quickly.

## Overview

- Set up your Openlyne API credentials
- Install dependencies
- Send your first WhatsApp message (Python, JavaScript, or curl)

---

## Prerequisites

- Python 3.7+ or Node.js 14+
- Text editor (VS Code recommended)
- Openlyne API account ([sign up](https://openlyne.com))

---

## 1. Get API Credentials

1. Sign up at [openlyne.com](https://openlyne.com)
2. Go to your dashboard
3. Copy your API Key (starts with `ol_`)
4. Copy your Project ID

---

## 2. Configure Environment Variables

Create a `.env` file in your project root:

```env
OPENLYNE_API_KEY=your_api_key_here
PROJECT_ID=your_project_id_here
```

> **Note:** Never commit `.env` files to git.

---

## 3. Install Dependencies

**Python:**

```bash
pip install requests python-dotenv
```

**JavaScript:**

```bash
npm install axios dotenv
```

---

## 4. Send Your First Message

Choose one of the following methods:

### Python

```bash
python setup.py
```

### JavaScript

```bash
node setup.js
```

### Curl

```bash
curl -X POST https://api.openlyne.com/v1/sendText \
    -H "x-api-key: your_api_key_here" \
    -H "Content-Type: application/json" \
    -d '{
    "phone_number": "256XXXXXXXXXX",
        "message": "Hello from my first WhatsApp bot!",
        "project_id": "your_project_id_here"
    }'
```

---

## 5. Check the Response

If successful, you'll see:

```json
{
    "success": true,
    "data": { /* details about the sent message */ },
    "message": "sent"
}
```

If there's an error:

```json
{
    "success": false,
    "data": { /* error details */ }
}
```

---

## Example Bot

Send a WhatsApp message to **256XXXXXXXXXX** to see a demo bot in action.

---

## Troubleshooting

**Invalid API key:**
- Check your API key in `.env`

**Project ID not found:**
- Verify your Project ID

**Module not found:**
- Reinstall dependencies

> For more help, see the [troubleshooting guide](../docs/troubleshooting.md) or contact support.

---

## Next Steps

Explore more features:
- Send different message types
- Format messages
- Send to multiple recipients

Continue to [Tutorial 02: Send Messages](../02-send-messages/)

---

## Support

- Email: sales@openlyne.com
- WhatsApp: 256XXXXXXXXXX
- Docs: [openlyne.com/docs](https://openlyne.com/docs)