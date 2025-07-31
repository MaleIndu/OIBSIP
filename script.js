function sendMessage() {
  const userInput = document.getElementById("userInput");
  const chatBox = document.getElementById("chatBox");

  if (userInput.value.trim() !== "") {
    // Add user's message
    const userMessage = document.createElement("div");
    userMessage.textContent = "You: " + userInput.value;
    chatBox.appendChild(userMessage);

    // Add bot reply
    const botMessage = document.createElement("div");
    botMessage.textContent = "Bot: " + generateReply(userInput.value);
    chatBox.appendChild(botMessage);

    chatBox.scrollTop = chatBox.scrollHeight;
    userInput.value = "";
  }
}

function generateReply(message) {
  const msg = message.toLowerCase();

  if (msg.includes("hi") || msg.includes("hello")) {
    return "Hello! How can I help you today?";
  } else if (msg.includes("bye")) {
    return "Goodbye! Have a great day!";
  } else if (msg.includes("time")) {
    return "⏰ The current time is: " + new Date().toLocaleTimeString();
  } else if (msg.includes("operating system")) {
    return "🖥️ An Operating System is system software that manages computer hardware, software, and resources.";
  } else if (msg.includes("python")) {
    return "🐍 Python is a popular programming language known for its simplicity and readability.";
  } else if (msg.includes("ai")) {
    return "🤖 AI (Artificial Intelligence) is the simulation of human intelligence by machines.";
  } else {
    return "I'm still learning! 🤖 Please ask something simple like 'what is Python?'";
  }
}
