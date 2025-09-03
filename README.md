# WhatsApp Chatbot API Tutorials

A collection of tutorials for building WhatsApp chatbots using the Openlyne API in Python and JavaScript.

[![API Status](https://img.shields.io/badge/API-Alpha-orange)](https://api.openlyne.com)
[![Support](https://img.shields.io/badge/Support-Email-blue)](mailto:sales@openlyne.com)
[![Countries](https://img.shields.io/badge/Countries-7-green)](#supported-countries)

## Overview

This repository provides step-by-step tutorials for developers who want to build WhatsApp chatbots using the [Openlyne API](https://openlyne.com). The tutorials are available in both Python and JavaScript, covering everything from basic message sending to advanced automation workflows.

Openlyne is a REST API designed for programmatically sending and receiving WhatsApp messages, with a focus on serving developers in Africa. The API is currently in alpha and supports Nigeria (+234), Kenya (+254), Uganda (+256), Rwanda (+250), Tanzania (+255), and Egypt (+20).

## Prerequisites

Before starting these tutorials, you'll need:

- Python 3.7+ or Node.js 14+
- An Openlyne API key and project ID (sign up at [openlyne.com](https://openlyne.com))
- A valid WhatsApp number in a supported country
- Basic familiarity with REST APIs and webhooks

## Quick Start

### 1. Clone this repository

```bash
git clone https://github.com/openlyne/whatsapp-chatbot-api.git
cd whatsapp-chatbot-api
```

### 2. Choose your language and install dependencies

**For Python:**
```bash
# Install Python dependencies
pip install requests python-dotenv
```

**For JavaScript:**
```bash
# Install Node.js dependencies  
npm init -y
npm install axios dotenv
```

### 3. Set up environment variables

Create a `.env` file in the root directory:

```bash
# .env
OPENLYNE_API_KEY=your_api_key_here
PROJECT_ID=your_project_id_here
```

### 4. Send your first message

**Python example:**
```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    "https://api.openlyne.com/v1/sendText",
    headers={
        "x-api-key": os.getenv("OPENLYNE_API_KEY"),
        "Content-Type": "application/json"
    },
    json={
    "number": "256XXXXXXXXXX",
        "message": "Hello from Openlyne!",
        "project_id": os.getenv("PROJECT_ID")
    }
)

print(response.json())
```

**JavaScript example:**
```javascript
require('dotenv').config();
const axios = require('axios');

async function sendMessage() {
    try {
        const response = await axios.post(
            'https://api.openlyne.com/v1/sendText',
            {
                number: '256XXXXXXXXXX',
                message: 'Hello from Openlyne!',
                project_id: process.env.PROJECT_ID
            },
            {
                headers: {
                    'x-api-key': process.env.OPENLYNE_API_KEY,
                    'Content-Type': 'application/json'
                }
            }
        );
        console.log(response.data);
    } catch (error) {
        console.error('Error:', error.response?.data || error.message);
    }
}

sendMessage();
```

## Tutorials

Follow these tutorials in order to build your WhatsApp chatbot skills:

- [**01. Getting Started**](./01-getting-started/) - Set up your development environment and send your first message
- [**02. Send Messages**](./02-send-message/) - Learn different ways to send text messages
- [**03. Receive Messages**](./03-receive-message/) - Handle incoming messages with webhooks
- [**04. Message Types**](./04-message-types/) - Work with images, documents, and media files
- [**05. Interactive Messages**](./05-interactive-messages/) - Add buttons, lists, and quick replies
- [**06. Error Handling**](./06-error-handling/) - Handle errors and edge cases gracefully
- [**07. Webhook Security**](./07-webhook-security/) - Secure your webhook endpoints
- [**08. Deploy Your Bot**](./08-deploy-your-bot/) - Deploy your chatbot to production
- [**09. Advanced Features**](./09-advanced-features/) - Templates, analytics, and automation

Each tutorial folder contains:
- Step-by-step instructions in the README
- Complete Python example (`example.py`)
- Complete JavaScript example (`example.js`)
- Any additional files needed

## API Reference

### Authentication
All API requests require an `x-api-key` header:

```bash
curl -X POST "https://api.openlyne.com/v1/sendText" \
  -H "x-api-key: your_api_key_here" \
  -H "Content-Type: application/json"
```

### Key Endpoints
- `POST /sendText` - Send a WhatsApp message
- `GET /status` - Check connection and device status  
- `GET /messages` - Retrieve message history
- `POST /webhook` - Configure webhook for incoming messages

### Required Parameters
- `number` - Recipient's WhatsApp number in E.164 format
- `message` - Message content (text)
- `project_id` - Your Openlyne project identifier

For complete API documentation, visit [openlyne.com/docs](https://openlyne.com/docs).

## Roadmap

- [x] 01. Getting Started — Setup and send your first message
- [ ] 02. Send Messages — Different ways to send text
- [ ] 03. Receive Messages — Handle incoming messages (webhooks)
- [ ] 04. Message Types — Images, documents, and media
- [ ] 05. Interactive Messages — Buttons, lists, quick replies
- [ ] 06. Error Handling — Graceful error handling and retries
- [ ] 07. Webhook Security — Secure your endpoints
- [ ] 08. Deploy Your Bot — Ship to production
- [ ] 09. Advanced Features — Templates, analytics, automation
- [ ] Examples — Echo bot, customer support bot
- [ ] Docs — API reference, troubleshooting, best practices

## Rate Limits & Constraints

**Current Alpha Limits:**

- 1 message per second
- 1,000 messages per day  
- 10,000 messages per month

**Supported Countries:**

- Nigeria (+234)
- Kenya (+254)
- Uganda (+256)
- Rwanda (+250)
- Tanzania (+255)
- Egypt (+20)

## Testing

Try the example chatbot by sending a WhatsApp message to **254101886585** to see how responses work in practice.

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes with tests
4. Ensure both Python and JavaScript versions work
5. Commit your changes: `git commit -am 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

### Guidelines

- Follow existing code style and structure
- Include working examples for both languages
- Add appropriate error handling
- Update documentation as needed
- Test thoroughly before submitting

## Security

**Important:** Never commit API keys or sensitive credentials to version control.

- Use environment variables for all secrets
- Add `.env` files to your `.gitignore`
- Use the provided `.env.example` files as templates
- For production, use secure secret management services

## Support

- **Documentation:** [openlyne.com/docs](https://openlyne.com/docs)
- **Support Email:** [sales@openlyne.com](mailto:sales@openlyne.com)
- **WhatsApp Support:** 254101886585
- **Example Bot:** Send a message to 254101886585

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The Openlyne API has its own terms of service available at [openlyne.com/terms](https://openlyne.com/terms).

---

**Questions?** Contact us at [sales@openlyne.com](mailto:sales@openlyne.com) or try our example bot at 254101886585.

## ⚠️ Important Disclaimers & Legal Information

**Development vs Production**: The tutorials use ngrok and other development tools that are **NOT suitable for production use**. Always use proper hosting and security measures for production deployments.

**Example Phone Numbers**: All phone numbers shown (like `256XXXXXXXXXX`) are examples only and not real numbers. Always replace with your actual test numbers and obtain explicit consent before sending messages.

**API Security**: Keep your API keys secure. Never commit them to version control or expose them in client-side code. Use environment variables and proper secret management.

**Legal Compliance**: By using this API, you agree to:
- [Openlyne Terms of Service](https://openlyne.com/terms)
- [Openlyne Privacy Policy](https://openlyne.com/privacy)
- WhatsApp Business API terms and policies
- All applicable data protection laws (GDPR, CCPA, etc.)

**User Consent**: Always obtain proper consent before sending WhatsApp messages. Respect user privacy and provide clear opt-out mechanisms.

**Rate Limits**: Respect API rate limits. Exceeding limits may result in temporary or permanent suspension of your API access.
