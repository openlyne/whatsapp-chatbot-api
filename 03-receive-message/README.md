# Tutorial 03: Receive WhatsApp Messages

Learn how to receive WhatsApp messages sent to your Openlyne number. We'll create a simple server that listens for incoming messages and displays them in your terminal.

## What You Need

- Completed Tutorial 01 (Getting Started)
- Openlyne API key and Project ID
- ngrok (we'll install this together)

## What You'll Build

A simple server that:

- Receives WhatsApp messages
- Shows them in your terminal
- Can be extended to send automatic replies

## ⚠️ Development Environment Warning

**ngrok is for Development Only**: This tutorial uses ngrok for testing purposes. **NEVER use ngrok or similar tunneling services in production environments** as they create security vulnerabilities.

**Webhook Security**: The basic webhook example has no authentication. For production use, implement proper webhook signature verification and authentication.

**Example Data**: Phone numbers like `256XXXXXXXXXX` in examples are placeholders only, not real numbers.

**Production Deployment**: For production, use proper hosting services with SSL certificates, not development tunnels.

---

## Step 1: Install ngrok

**Important**: Openlyne requires a secure HTTPS URL for webhooks. ngrok creates this for you automatically.

### Option A: Download from Website

1. Go to [ngrok.com](https://ngrok.com) and create a free account
2. Download ngrok for your operating system:
   - **Mac**: Download the ZIP file
   - **Windows**: Download the ZIP file
   - **Linux**: Download the appropriate package

3. Extract the downloaded file
4. Move ngrok to a folder in your PATH (optional but recommended):

```bash
# On Mac/Linux
sudo mv ngrok /usr/local/bin/

# On Windows, add the folder containing ngrok.exe to your PATH
```

### Option B: Install with Package Manager

**Mac (using Homebrew):**

```bash
brew install ngrok/ngrok/ngrok
```

**Windows (using Chocolatey):**

```bash
choco install ngrok
```

**Linux (using apt):**

```bash
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
sudo apt update && sudo apt install ngrok
```

### Verify Installation

```bash
ngrok --version
```

You should see: `ngrok version 3.x.x`

### Authenticate ngrok

1. Get your auth token from [ngrok.com/your-authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)
2. Add it to ngrok:

```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN_HERE
```

---

## Step 2: Create Your Message Receiver

Choose either Python or JavaScript:

### Option A: Python (easier for beginners)

Install what you need:

```bash
pip install fastapi uvicorn
```

Run your server:

```bash
python receive.py
```

### Option B: JavaScript

Install what you need:

```bash
npm install express
```

Run your server:

```bash
node receive.js
```

You'll see: `🚀 Starting WhatsApp webhook server...`

---

## Step 3: Make Your Server Public with ngrok

**⚠️ DEVELOPMENT ONLY**: ngrok is a development tool. Never use it for production applications.

**Why ngrok?** Openlyne requires a secure HTTPS URL for webhooks. ngrok automatically provides this **for testing purposes only**.

### Start ngrok

Open a **new terminal** (keep your server running in the first one) and run:

```bash
ngrok http 8000
```

**Security Warning**: This creates a public tunnel to your local machine. Only use this in development environments with test data.

You'll see something like:

```text
Forwarding        https://abc123.ngrok.io -> http://localhost:8000
```

**Important**:

- Copy that `https://abc123.ngrok.io` URL - you'll need it!
- Notice it's **HTTPS** (secure) - this is required by Openlyne
- Keep this terminal open while testing

---

## Step 4: Connect to Openlyne

1. Go to your [Openlyne Dashboard](https://openlyne.com/dashboard)
2. Find your project settings
3. Look for "Webhook URL"
4. Enter your ngrok URL + `/webhook`:

   ```text
   https://abc123.ngrok.io/webhook
   ```

5. Save it

## Step 5: Test It

1. Send a WhatsApp message to your Openlyne number
2. Look at your terminal where the server is running
3. You should see the message data:

```text
📱 New message: {
  "key": {
    "remoteJid": "256XXXXXXXXXX@s.whatsapp.net",
    "fromMe": false,
    "id": "message_id_here"
  },
  "pushName": "John",
  "messageType": "conversation",
  "message": {
    "conversation": "Hello!"
  },
  "messageTimestamp": 1693834567
}
```

🎉 **Success!** You can now see the message data that Openlyne sends!

## What's Next

Now that you can receive messages, you can:

- **Tutorial 04**: Build a bot that replies automatically  
- **Examples**: Check out complete chatbots in the `examples/` folder
- **Customize**: Add your own logic to the code files

## Need Help

**ngrok not working?**

- Make sure you signed up at ngrok.com and got your auth token
- Run `ngrok config add-authtoken YOUR_TOKEN` first
- Check that your server is running before starting ngrok

**Not receiving messages?**

- Double-check your webhook URL in the Openlyne dashboard
- Make sure your URL starts with `https://` (HTTP won't work!)
- Verify both your server and ngrok are running
- Try sending a test message

**Getting "invalid URL" errors?**

- Openlyne only accepts HTTPS URLs
- Make sure you're using the `https://` URL from ngrok, not `http://`
- Don't use `localhost` URLs - they won't work

**Still stuck?**

- Check the ngrok web interface at `http://127.0.0.1:4040`
- Look for error messages in your terminal
- Make sure your ngrok auth token is set up correctly
