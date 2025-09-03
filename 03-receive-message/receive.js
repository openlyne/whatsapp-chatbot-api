const express = require('express');
const app = express();
const PORT = 8000;

// This helps Express understand JSON data
app.use(express.json());

// This function receives WhatsApp messages from Openlyne
app.post('/webhook', (req, res) => {
    const payload = req.body;
    
    // Check if this is a new message
    if (payload.event === 'messages.upsert') {
        const data = payload.data || {};
        console.log(`📱 New message: ${JSON.stringify(data, null, 2)}`);
    }
    
    // Add your response logic here
    // For example: send a reply, save to database, etc.
    // Call the function send_text(data.key.remoteJid, "Hello from Openlyne!");

    res.json({ status: 'received' });
});

// Start the server
app.listen(PORT, '0.0.0.0', () => {
    console.log('🚀 Starting Openlyne webhook server...');
    console.log(`🔗 Webhook URL: http://localhost:${PORT}/webhook`);
});

module.exports = app;