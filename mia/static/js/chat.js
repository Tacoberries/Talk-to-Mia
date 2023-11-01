// chatbot_app/static/js/chatbot.js
document.addEventListener('DOMContentLoaded', function() {
    const chatContainer = document.getElementById('chat-container');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    sendButton.addEventListener('click', function() {
        const userMessage = userInput.value;
        console.log("Botão Clicado. Mensagem enviada: ",{userMessage});
        userInput.value = ''; // Limpa o campo de entrada


        // Função para obter o token CSRF do cookie
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === name + '=') {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        // Obter o token CSRF
        const csrftoken = getCookie('csrftoken');
        
        // Enviar a pergunta do usuário para o servidor Django
        fetch('/api/mia/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ user_message: userMessage }),
        })
        .then(response => response.json())
        .then(data => {
            const chatbotResponse = data.mia_response;
            const intent = data.intent;
            chatContainer.innerHTML += `<p><strong>Você:</strong> ${userMessage}</p>`;
            chatContainer.innerHTML += `<p><strong>Mia:</strong> ${chatbotResponse}</p>`;
            console.log(intent);
        });
        
    });
});
