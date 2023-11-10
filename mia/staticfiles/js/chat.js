document.addEventListener('DOMContentLoaded', function() {
    const chatContainer = document.getElementById('chat-container');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    sendButton.addEventListener('click', function() {
        const userMessage = userInput.value;    
        userInput.value = ''; // Limpa o campo de entrada

        // Enviar a pergunta do usuário para o servidor Django
        fetch('/api/mia/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_message: userMessage }),
        })
        .then(response => response.json())
        .then(data => {
            const chatbotResponse = data.mia_response;
            // Exibir a resposta do chatbot no chatContainer
            chatContainer.innerHTML += `<p><strong>Você:</strong> ${userMessage}</p>`;
            chatContainer.innerHTML += `<p><strong>Chatbot:</strong> ${chatbotResponse}</p>`;
            console.log("Resposta dada")
        });
    });
});