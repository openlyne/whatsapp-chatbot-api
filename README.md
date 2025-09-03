# WhatsApp Chatbot API Tutorials

A collection of tutorials for building WhatsApp chatbots using the Openlyne API in Python and JavaScript.

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
    "phone_number": "256XXXXXXXXXX",
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
                phone_number: '256XXXXXXXXXX',
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
- [**02. Send Messages**](./02-send-messages/) - Learn different ways to send text messages
- [**03. Receive Messages**](./03-receive-messages/) - Handle incoming messages with webhooks
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
- `phone_number` - Recipient's WhatsApp number in E.164 format
- `message` - Message content (text)
- `project_id` - Your Openlyne project identifier

For complete API documentation, visit [openlyne.com/docs](https://openlyne.com/docs).

## Repository Structure

```
whatsapp-chatbot-api/
├── README.md                           # This file
├── LICENSE                             # License information
├── .env.example                        # Environment variables template
├── .gitignore                         # Git ignore rules
├── 01-getting-started/                # Tutorial 1: Setup and first message
│   ├── README.md                      # Step-by-step instructions
│   ├── setup.py                       # Python version
│   └── setup.js                       # JavaScript version
├── 02-send-messages/                  # Tutorial 2: Sending messages
│   ├── README.md
│   ├── send-message.py
│   └── send-message.js
├── 03-receive-messages/               # Tutorial 3: Receiving messages
│   ├── README.md
│   ├── webhook.py
│   └── webhook.js
├── 04-message-types/                  # Tutorial 4: Media and file types
│   ├── README.md
│   ├── media-messages.py
│   └── media-messages.js
├── 05-interactive-messages/           # Tutorial 5: Buttons and menus
│   ├── README.md
│   ├── interactive.py
│   └── interactive.js
├── 06-error-handling/                 # Tutorial 6: Error handling
│   ├── README.md
│   ├── error-handling.py
│   └── error-handling.js
├── 07-webhook-security/               # Tutorial 7: Security
│   ├── README.md
│   ├── secure-webhook.py
│   └── secure-webhook.js
├── 08-deploy-your-bot/               # Tutorial 8: Deployment
│   ├── README.md
│   ├── deploy.py
│   └── deploy.js
├── 09-advanced-features/             # Tutorial 9: Advanced topics
│   ├── README.md
│   ├── advanced.py
│   └── advanced.js
├── examples/                         # Complete example projects
│   ├── echo-bot/
│   │   ├── echo-bot.py
│   │   └── echo-bot.js
│   └── customer-support-bot/
│       ├── support-bot.py
│       └── support-bot.js
└── docs/                            # Additional documentation
    ├── api-reference.md
    ├── troubleshooting.md
    └── best-practices.md
```

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

Try the example chatbot by sending a WhatsApp message to **256XXXXXXXXXX** to see how responses work in practice.

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
- **Support Email:** sales@openlyne.com
- **WhatsApp Support:** 256XXXXXXXXXX
- **Example Bot:** Send a message to 256XXXXXXXXXX

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The Openlyne API has its own terms of service available at [openlyne.com/terms](https://openlyne.com/terms).

---

**Questions?** Contact us at sales@openlyne.com or try our example bot at 256XXXXXXXXXX.