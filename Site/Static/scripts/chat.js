function sendMessage() {
  let message = document.getElementById("user_input").value;

  if (message.length > 0) {
    const userChat = document.createElement("div");
    const chatContainer = document.querySelector(".chat-container");

    userChat.classList.add("user-chat");
    userChat.innerHTML = `<p>${message}</p>`;

    chatContainer.appendChild(userChat);

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
        const chatContainer = document.querySelector(".chat-container");
        const aiChat = document.createElement("div");

        aiChat.classList.add("ai-chat");
        aiChat.innerHTML = `<p>${data.message}</p>`;

        chatContainer.appendChild(aiChat);
      });
  } else {
    const chatDiv = document.getElementById("chat");
    chatDiv.innerText = "must put in at least one letter";
  }
}
