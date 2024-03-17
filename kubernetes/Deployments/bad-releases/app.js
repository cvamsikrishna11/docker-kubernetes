// app.js

const express = require('express');
const app = express();
let requestCount = 0;

app.get('/', (req, res) => {
    if (++requestCount > 3) {
        console.error('Simulated crash after 3 requests');
        process.exit(1); // Simulate crash
    }

    res.sendFile('index.html', { root: __dirname });
});

app.listen(8080, () => {
    console.log('Server running on port 8080');
});
