const axios = require("axios");

function send_text(phone, text) {
  const response = axios.post(
    "https://api.openlyne.com/v1/sendText",
    {
      number: phone,
      message: text,
      project_id: "PROJECT_ID",
    },
    {
      headers: { "x-api-key": "OPENLYNE_API_KEY" },
    }
  );

  console.log("Message sent!");
  return response;
}

// Example use
send_text("256XXXXXXXXXX", "Hello from Openlyne!");
