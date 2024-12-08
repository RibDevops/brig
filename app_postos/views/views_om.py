
from django.shortcuts import render, redirect, get_object_or_404
from app_cert.models import Om
from ..forms import OmForm
from django.db.models import Count
from django.contrib import messages
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.decorators import login_required



@login_required
def scp_om_lista(request):
    # Consulta para obter todas as OM ordenadas por força/orgão
    dataset = (
        Om.objects
        .values('fk_forca_orgao', 'fk_forca_orgao__forca_orgao' )  
            .annotate(total=Count('fk_forca_orgao'))  
            .prefetch_related('fk_forca_orgao')
        )
    
    print(dataset)
    context = {"dataset": dataset}
    return render(request, 'om/lista.html', context)

@login_required
def scp_om_detalhes(request, id):
    # Obtém a instância da Om com o ID fornecido ou retorna um erro 404 caso não exista
    # om = get_object_or_404(Om, pk=id)

    # Filtra o conjunto de dados de Om com base na OM específica
    dataset = Om.objects.filter(fk_forca_orgao=id)

    context = {
        "dataset": dataset,
        # "om": om  # Passa a instância de Om para o contexto
    }
    return render(request, 'om/lista_om.html', context)

@login_required
def scp_om_nova(request):
    if request.method == 'POST':
        form = OmForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Om cadastrada com sucesso.')
            return redirect('scp_om_lista')  # Redirecione para a lista após criar
    else:
        form = OmForm()
    
    return render(request, 'om/criar.html', {'form': form})

@login_required
def scp_om_editar(request, id):
    context ={}
    om_ob = get_object_or_404(Om, id=id)
    if request.method == 'POST':
        form = OmForm(request.POST, instance=om_ob)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Om editada com sucesso.')
            return redirect('scp_om_lista')
    else:
        form = OmForm(instance=om_ob)
    context = {
        'form': form,
        'om_ob': om_ob
    }
    return render(request, 'om/editar.html', context)

@login_required
def scp_om_delete(request, id):
    context ={}
    om_ob = get_object_or_404(Om, id=id)
    if request.method == 'POST':
        om_ob.delete()
        messages.add_message(request, messages.SUCCESS, 'Om excluída com sucesso.') 
        return redirect('scp_om_lista')
    
    context = {
        'om_ob': om_ob
    }
    
    return render(request, 'om/excluir.html', context)


# def sgc_ano_detalhes(request, pk):
#     ano_ob = get_object_or_404(Om, pk=pk)
#     return render(request, 'om/detalhes.html', {'ano_ob': ano_ob})
