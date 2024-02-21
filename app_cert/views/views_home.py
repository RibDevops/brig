from django.shortcuts import render
from requests import request

def sgc_home(request):
    # context = gera_menu()  # Mescla o contexto existente com o novo contexto
    return render(request, 'sgc_home.html')
