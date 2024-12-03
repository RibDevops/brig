from django.shortcuts import render, redirect, get_object_or_404
from requests import request
from ..models import Instrucao
from ..forms import InstrucaoForm # Importe o formulário adequado
from django.contrib import messages
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.decorators import login_required


@login_required
def sgc_instrucao_nova(request):
    if request.method == 'POST':
        form = InstrucaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Instrução cadastrada com sucesso.')
            return redirect('sgc_instrucao_lista')  # Redirecione para a lista após criar
    else:
        form = InstrucaoForm()
    
    return render(request, 'instrucao/criar.html', {'form': form})

@login_required
def sgc_instrucao_lista(request):
    dataset = Instrucao.objects.all()
    # dataset = Instrucao.objects.select_related('fk_turma', 'fk_in_ex', ).all()
    context = {"dataset": dataset}
    print(dataset)
    return render(request, 'instrucao/lista.html', context)

@login_required
def sgc_instrucao_editar(request, id):
    context ={}
    instrucao_ob = get_object_or_404(Instrucao, id=id)
    if request.method == 'POST':
        form = InstrucaoForm(request.POST, instance=instrucao_ob)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Instrução editada com sucesso.')
            return redirect('sgc_instrucao_lista')
    else:
        form = InstrucaoForm(instance=instrucao_ob)
    context = {
        'form': form,
        'instrucao_ob': instrucao_ob
    }
    return render(request, 'instrucao/editar.html', context)

@login_required
def sgc_instrucao_delete(request, id):
    context ={}
    instrucao_ob = get_object_or_404(Instrucao, id=id)
    if request.method == 'POST':
        instrucao_ob.delete()
        messages.add_message(request, messages.SUCCESS, 'Instrução excluída com sucesso.') 
        return redirect('sgc_instrucao_lista')
    
    context = {
        'instrucao_ob': instrucao_ob
    }
    
    return render(request, 'instrucao/excluir.html', context)

