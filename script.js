async function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    if (!userInput) return;

    const messagesDiv = document.getElementById("messages");

    // Adiciona a mensagem do usuário
    const userMessage = document.createElement("div");
    userMessage.classList.add("message", "user-message");
    userMessage.textContent = userInput;
    messagesDiv.appendChild(userMessage);

    // Limpa o campo de entrada
    document.getElementById("userInput").value = "";

    // Faz a requisição ao backend
    try {
        const response = await fetch ("https://meu-chatbot.onrender.com/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt: userInput })
        });

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.statusText}`);
        }

        const data = await response.json();

        // Adiciona a resposta do Gemini
        const botMessage = document.createElement("div");
        botMessage.classList.add("message", "bot-message");
        botMessage.textContent = data.response;
        messagesDiv.appendChild(botMessage);

    } catch (error) {
        console.error("Erro:", error);
    }

    // Faz scroll para a última mensagem
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}
