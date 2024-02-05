function sendMessage() {
  const messageInput = document.getElementById('message-input');
  const chatContainer = document.getElementById('chat-container');

  const userMessage = messageInput.value;

  if (userMessage.trim() !== '') {
    // Display user's message
    chatContainer.innerHTML += `<div><strong>You:</strong> ${userMessage}</div>`;

    // Simulate a response (you can replace this with actual server communication)
    setTimeout(() => {
      const responseMessage = "I'm a simple chat bot!";
      chatContainer.innerHTML += `<div><strong>Bot:</strong> ${responseMessage}</div>`;
    }, 1000);

    // Clear the input field
    messageInput.value = '';

    // Scroll to the bottom of the chat
    chatContainer.scrollTop = chatContainer.scrollHeight;
  }
}