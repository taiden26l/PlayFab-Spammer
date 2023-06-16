const axios = require('axios');

const url = 'http://example.com/your-endpoint';
const payload = { key: 'value' };

async function sendRequest() {
  try {
    const response = await axios.post(url, payload);
    // Process the response if needed
    sendRequest(); // Recursively call the function for infinite loop
  } catch (error) {
    // Handle error if needed
    sendRequest(); // Recursively call the function for infinite loop
  }
}

// Start the infinite loop
sendRequest();
