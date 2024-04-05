function sendMessage() {
  let message = document.getElementById("user_input").value;

  if (message.length > 0) {
    document.getElementById("user_input").value = "";
    fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: message }),
    })
      .then((response) => response.json())
      .then((data) => {
        const chatDiv = document.getElementById("chat");
        const userDiv = document.createElement("div");
        userDiv.innerText = "You: " + message;
        chatDiv.appendChild(userDiv);
        const botDiv = document.createElement("div");
        botDiv.innerText = "Bot: " + data.message;
        chatDiv.appendChild(botDiv);
      });
  } else {
    const chatDiv = document.getElementById("chat");
    chatDiv.innerText = "must put in at least one letter";
  }
}
