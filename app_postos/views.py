from django.shortcuts import render

# Create your views here.
def home(request):
    # context = gera_menu()  # Mescla o contexto existente com o novo contexto
    # return render(request, 'home.html', context )
    return render(request, 'sgu_home.html')