const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.post('/get-response', (req, res) => {
    const userInput = req.body.text;
    const pythonProcess = spawn('python', ['D:\Programming\Project\main.py', userInput]);

    pythonProcess.stdout.on('data', (data) => {
        const response = data.toString();
        res.send({ response });
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
