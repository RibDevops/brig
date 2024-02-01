
from django.shortcuts import render, redirect, get_object_or_404
from app_cert.models import Forca_Orgao
from ..forms import ForcaForm
from django.db.models import Count
from django.contrib import messages

def scp_forca_lista(request):
    # Consulta para obter todas as OM ordenadas por força/orgão
    dataset = (
        Forca_Orgao.objects
        .values('fk_forca_orgao', 'fk_forca_orgao__forca_orgao' )  
            .annotate(total=Count('fk_forca_orgao'))  
            .prefetch_related('fk_forca_orgao')
        )
    
    print(dataset)
    context = {"dataset": dataset}
    return render(request, 'om/lista.html', context)

def scp_forca_detalhes(request, id):
    # Obtém a instância da Om com o ID fornecido ou retorna um erro 404 caso não exista
    # om = get_object_or_404(Om, pk=id)

    # Filtra o conjunto de dados de Om com base na OM específica
    dataset = Forca_Orgao.objects.filter(fk_forca_orgao=id)

    context = {
        "dataset": dataset,
        # "om": om  # Passa a instância de Om para o contexto
    }
    return render(request, 'om/lista_om.html', context)


def scp_forca_nova(request):
    if request.method == 'POST':
        form = ForcaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cadastrada com sucesso.')
            return redirect('scp_om_lista')  # Redirecione para a lista após criar
    else:
        form = ForcaForm()
    
    return render(request, 'om/criar.html', {'form': form})

def scp_forca_ditar(request, id):
    context ={}
    om_ob = get_object_or_404(Forca_Orgao, id=id)
    if request.method == 'POST':
        form = ForcaForm(request.POST, instance=om_ob)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Editada com sucesso.')

            return redirect('scp_om_lista')
    else:
        form = ForcaForm(instance=om_ob)
    context = {
        'form': form,
        'om_ob': om_ob
    }
    return render(request, 'om/editar.html', context)

def scp_forca_delete(request, id):
    context ={}
    om_ob = get_object_or_404(Forca_Orgao, id=id)
    if request.method == 'POST':
        om_ob.delete()
        messages.add_message(request, messages.SUCCESS, 'Excluída com sucesso.') 
        return redirect('scp_om_lista')
    
    context = {
        'om_ob': om_ob
    }
    
    return render(request, 'om/excluir.html', context)


# def sgc_ano_detalhes(request, pk):
#     ano_ob = get_object_or_404(Om, pk=pk)
#     return render(request, 'om/detalhes.html', {'ano_ob': ano_ob})
