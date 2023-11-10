from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . import logic
import json


# chatbot_app/views.py
from django.http import JsonResponse

def mia_api(request):
    if request.method == 'POST':
        # Lê o corpo JSON da solicitação
        data = json.loads(request.body)
        user_message = data.get('user_message', '')  # Use a chave 'user_message' do corpo JSON

        # Adicionar informações de depuração
        print(f"User Message: {user_message}")
        
        intent = logic.classify_intent(user_message)

        # Adicionar informações de depuração
        print(f"Intent: {intent}")

        mia_response = logic.generate_response(intent)

        # Adicionar informações de depuração
        print(f"Mia Response: {mia_response}")

        return JsonResponse({'mia_response': mia_response})





def home(request):

    return render(request, 'mia/home.html')

def about(request):
    return render(request, 'mia/about.html')
