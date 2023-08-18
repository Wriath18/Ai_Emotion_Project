// JavaScript code for interacting with the chatbot
const chatBox = document.getElementById('chatBox');
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');

sendButton.addEventListener('click', () => {
    const userMessage = userInput.value;
    if (userMessage.trim() !== '') {
        addMessage('User', userMessage);
        // Send userMessage to your backend for processing (AJAX request, etc.)
        // Receive botResponse from the backend
        const botResponse = 'This is a sample bot response.';
        addMessage('Bot', botResponse);
        userInput.value = '';
    }
});

function addMessage(sender, message) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender.toLowerCase()}-message`;
    messageDiv.textContent = `${sender}: ${message}`;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}
