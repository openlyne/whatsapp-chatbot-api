# Tutorial 01: Getting Started

Welcome to your first WhatsApp chatbot tutorial! In this tutorial, you'll set up your development environment and send your very first WhatsApp message using the Openlyne API.

## What You'll Learn

- How to set up your Openlyne API credentials
- How to install the required dependencies
- How to send your first WhatsApp message
- How to handle basic errors

## Prerequisites

- Python 3.7+ OR Node.js 14+
- A text editor (VS Code, Sublime, etc.)
- An Openlyne API account ([sign up here](https://openlyne.com))

## Step 1: Get Your API Credentials

1. Go to [openlyne.com](https://openlyne.com) and sign up for an account
2. Once logged in, navigate to your dashboard
3. Copy your **API Key** (starts with `ol_`)
4. Copy your **Project ID**

Keep these safe - you'll need them in the next step!

## Step 2: Set Up Environment Variables

Create a `.env` file in the root of this repository:

```bash
# .env
OPENLYNE_API_KEY=your_api_key_here
PROJECT_ID=your_project_id_here
```

**Important:** Never commit your `.env` file to git! It contains your secret API key.

## Step 3: Install Dependencies

Choose your preferred language:

### For Python:
```bash
pip install requests python-dotenv
```

### For JavaScript:
```bash
npm install axios dotenv
```

## Step 4: Send Your First Message

Now you're ready to send your first WhatsApp message! You can use either the Python or JavaScript version below.

### Python Version

Run the Python script:
```bash
python setup.py
```

### JavaScript Version

Run the JavaScript script:
```bash
node setup.js
```

## Step 5: Test It!

1. Run your chosen script
2. Check the console output - you should see a success response
3. Check your WhatsApp - you should receive the test message!

## Expected Output

If everything works correctly, you should see something like:
```json
{
    "success": true,
    "message_id": "msg_12345",
    "status": "sent",
    "timestamp": "2025-01-01T12:00:00Z"
}
```

## Try the Example Bot

Want to see how a real chatbot responds? Send a message to **+254101886585** and see it in action!

## Troubleshooting

### Common Issues:

**"Invalid API key"**
- Double-check your API key in the `.env` file
- Make sure there are no extra spaces or quotes

**"Project ID not found"**
- Verify your Project ID is correct
- Make sure you're using the right project

**"Phone number invalid"**
- Use E.164 format: 254101886585
- Make sure the country code is supported

**"Module not found"**
- Run the install commands again
- Make sure you're in the right directory

### Still Having Issues?

- Contact support: sales@openlyne.com
- Try the example bot: +254101886585
- Check the [troubleshooting guide](../docs/troubleshooting.md)

## What's Next?

Great job! You've successfully sent your first WhatsApp message. 

In the next tutorial, you'll learn:
- Different types of messages you can send
- How to format messages nicely
- How to send messages to multiple recipients

**Continue to [Tutorial 02: Send Messages](../02-send-messages/)**

## Need Help?

- **Email Support:** sales@openlyne.com
- **WhatsApp Support:** +254101886585
- **Documentation:** [openlyne.com/docs](https://openlyne.com/docs)