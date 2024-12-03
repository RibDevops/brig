
from django.shortcuts import render, redirect, get_object_or_404
from app_cert.models import Forca_Orgao
from ..forms import ForcaForm
from django.db.models import Count
from django.contrib import messages
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.decorators import login_required




@login_required
def scp_forca_lista(request):
    # Consulta para obter todas as OM ordenadas por força/orgão
    dataset = (
        Forca_Orgao.objects
        .values('forca_orgao', 'id', 'forca_orgao_descricao')  
            .annotate(total=Count('forca_orgao'))  
            .prefetch_related('forca_orgao')
        )
    
    print(dataset)
    context = {"dataset": dataset}
    return render(request, 'forca/lista.html', context)

@login_required
def scp_forca_detalhes(request, id):
    # Obtém a instância da Om com o ID fornecido ou retorna um erro 404 caso não exista
    # om = get_object_or_404(Om, pk=id)

    # Filtra o conjunto de dados de Om com base na OM específica
    dataset = Forca_Orgao.objects.filter(forca_orgao=id)

    context = {
        "dataset": dataset,
        # "om": om  # Passa a instância de Om para o contexto
    }
    return render(request, 'forca/lista_detalhes.html', context)

@login_required
def scp_forca_nova(request):
    if request.method == 'POST':
        form = ForcaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cadastrada com sucesso.')
            return redirect('scp_forca_lista')  # Redirecione para a lista após criar
    else:
        form = ForcaForm()
    
    return render(request, 'forca/criar.html', {'form': form})

@login_required
def scp_forca_editar(request, id):
    context ={}
    forca_ob = get_object_or_404(Forca_Orgao, id=id)
    if request.method == 'POST':
        form = ForcaForm(request.POST, instance=forca_ob)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Editada com sucesso.')

            return redirect('scp_forca_lista')
    else:
        form = ForcaForm(instance=forca_ob)
    context = {
        'form': form,
        'forca_ob': forca_ob
    }
    return render(request, 'forca/editar.html', context)

from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.decorators import has_permission_decorator


@login_required
def scp_forca_delete(request, id):
    context ={}
    forca_ob = get_object_or_404(Forca_Orgao, id=id)
    if request.method == 'POST':
        forca_ob.delete()
        messages.add_message(request, messages.SUCCESS, 'Excluída com sucesso.') 
        return redirect('scp_forca_lista')
    
    context = {
        'forca_ob': forca_ob
    }
    
    return render(request, 'forca/excluir.html', context)


# def sgc_ano_detalhes(request, pk):
#     ano_ob = get_object_or_404(Om, pk=pk)
#     return render(request, 'om/detalhes.html', {'ano_ob': ano_ob})
