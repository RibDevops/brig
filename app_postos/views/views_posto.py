
from django.shortcuts import render, redirect, get_object_or_404
from app_cert.models import Posto
from ..forms import PostoForm
from django.db.models import Count
from django.contrib import messages

from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('lista')
def scp_posto_lista(request):
    # Consulta para obter todas as OM ordenadas por força/orgão
    dataset = (
        Posto.objects
        .values('fk_forca_orgao', 'fk_forca_orgao__forca_orgao' )  
            .annotate(total=Count('fk_forca_orgao'))  
            .prefetch_related('fk_forca_orgao')
        )
    
    print(dataset)
    context = {"dataset": dataset}
    return render(request, 'posto/lista.html', context)

@has_permission_decorator('lista')
def scp_posto_detalhes(request, id):
    # Obtém a instância da Posto com o ID fornecido ou retorna um erro 404 caso não exista
    # om = get_object_or_404(Posto, pk=id)

    # Filtra o conjunto de dados de Posto com base na OM postocífica
    dataset = Posto.objects.filter(fk_forca_orgao=id)

    context = {
        "dataset": dataset,
        # "om": om  # Passa a instância de Posto para o contexto
    }
    return render(request, 'posto/lista_posto.html', context)

@has_permission_decorator('novo')
def scp_posto_novo(request):
    if request.method == 'POST':
        form = PostoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Posto cadastrado com sucesso.')
            return redirect('scp_posto_lista')  # Redirecione para a lista após criar
    else:
        form = PostoForm()
    
    return render(request, 'posto/criar.html', {'form': form})

@has_permission_decorator('editar')
def scp_posto_editar(request, id):
    context ={}
    posto_ob = get_object_or_404(Posto, id=id)
    if request.method == 'POST':
        form = PostoForm(request.POST, instance=posto_ob)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Posto editado com sucesso.')
            return redirect('scp_posto_lista')
    else:
        form = PostoForm(instance=posto_ob)
    context = {
        'form': form,
        'posto_ob': posto_ob
    }
    return render(request, 'posto/editar.html', context)

@has_permission_decorator('excluir')
def scp_posto_delete(request, id):
    context ={}
    posto_ob = get_object_or_404(Posto, id=id)
    if request.method == 'POST':
        posto_ob.delete()
        messages.add_message(request, messages.SUCCESS, 'Posto excluído com sucesso.')
        return redirect('scp_posto_lista')
    
    context = {
        'posto_ob': posto_ob
    }
    
    return render(request, 'posto/excluir.html', context)


# def sgc_ano_detalhes(request, pk):
#     ano_ob = get_object_or_404(Posto, pk=pk)
#     return render(request, 'posto/detalhes.html', {'ano_ob': ano_ob})
