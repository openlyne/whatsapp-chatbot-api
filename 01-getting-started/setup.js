#!/usr/bin/env node
/**
 * Tutorial 01: Getting Started - JavaScript Version
 * Send your first WhatsApp message using the Openlyne API
 */

require("dotenv").config();
const axios = require("axios");

async function main() {
  const apiKey = process.env.OPENLYNE_API_KEY;
  const projectId = process.env.PROJECT_ID;
  const url = "https://api.openlyne.com/v1/sendMessage";
  const headers = {
    "x-api-key": apiKey,
    "Content-Type": "application/json",
  };
  const data = {
    number: "254101886585", // Replace with the recipient's phone number in international format
    message: "Hello from my first WhatsApp bot!",
    project_id: projectId,
  };
  const response = await axios.post(url, data, { headers });
  console.log(response.data);
}

main();
