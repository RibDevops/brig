from django.shortcuts import render, redirect, get_object_or_404
from ..models import Tipo
from ..forms import TipoForm
# from django.urls.conf import include
# from django.urls import path

# app_name = 'views_tipo'  # Adicione esta linha

# urlpatterns = [
#     # URL padrão
#     path('', include('app_cert.views_curso', namespace='views_curso')),
# ]

def home(request):
    # context = gera_menu()  # Mescla o contexto existente com o novo contexto
    return render(request, 'home.html')

def tipo_novo(request):
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipo_lista')  # Redirecione para a lista após criar
    else:
        form = TipoForm()
    
    return render(request, 'tipo/criar.html', {'form': form})

def tipo_lista(request):
    dataset = Tipo.objects.all()
    context = {"dataset": dataset}
    # print(dataset)
    return render(request, 'tipo/lista.html', context)


# def tipo_detalhes(request, pk):
#     tipo_ob = get_object_or_404(TipoForm, pk=pk)
#     return render(request, 'tipo/detalhes.html', {'tipo_ob': tipo_ob})

def tipo_editar(request, id):
    context ={}
    tipo_ob = get_object_or_404(Tipo, id=id)
    if request.method == 'POST':
        form = TipoForm(request.POST, instance=tipo_ob)
        if form.is_valid():
            form.save()
            return redirect('tipo_lista')
    else:
        form = TipoForm(instance=tipo_ob)
    context = {
        'form': form,
        'tipo_ob': tipo_ob
    }
    return render(request, 'tipo/editar.html', context)

def tipo_delete(request, id):
    context ={}
    tipo_ob = get_object_or_404(Tipo, id=id)
    if request.method == 'POST':
        tipo_ob.delete()
        # messages.success(request, 'Registro excluído com sucesso.')
        return redirect('tipo_lista')
    
    context = {
        'tipo_ob': tipo_ob
    }
    
    return render(request, 'tipo/excluir.html', context)

