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

    try {
        // Mostra mensagem temporária enquanto espera a resposta
        const loadingMessage = document.createElement("div");
        loadingMessage.classList.add("message", "bot-message");
        loadingMessage.textContent = "Digitando...";
        messagesDiv.appendChild(loadingMessage);

        // Faz a requisição ao backend
        const response = await fetch("https://meu-chatbot-3.onrender.com/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt: userInput })
        });

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.statusText}`);
        }

        const data = await response.json();

        // Remove a mensagem de carregamento
        loadingMessage.remove();

        // Cria o elemento para a resposta do bot
        const botMessage = document.createElement("div");
        botMessage.classList.add("message", "bot-message");
        messagesDiv.appendChild(botMessage);

        // Efeito de digitação: adiciona a resposta letra por letra
        let i = 0;
        function typeWriter() {
            if (i < data.response.length) {
                botMessage.textContent += data.response.charAt(i);
                i++;
                setTimeout(typeWriter, 20); // ajuste a velocidade conforme necessário
            }
        }
        typeWriter();

    } catch (error) {
        console.error("Erro:", error);
    }

    // Faz scroll para a última mensagem
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}
