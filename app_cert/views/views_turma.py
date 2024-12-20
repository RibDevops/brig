from django.shortcuts import render, redirect, get_object_or_404
from requests import request
from ..models import Turma, Aluno
from ..forms import TurmaForm
from django.contrib import messages
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.decorators import login_required

@login_required
def sgc_turma_nova(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Turma cadastrada com sucesso.')
            return redirect('sgc_turma_lista')  # Redirecione para a lista após criar
    else:
        form = TurmaForm()
    
    return render(request, 'turma/criar.html', {'form': form})

@login_required
def sgc_turma_lista(request):
    # dataset = Turma.objects.all()
    dataset = Turma.objects.select_related(
        'fk_curso',
        'fk_tipo'
        ).all()
    context = {"dataset": dataset}
    
    alunos_da_turma = Aluno.objects.filter(fk_turma='1')
    print(alunos_da_turma )

    alunos_campos_faltando = []
    
    for aluno in alunos_da_turma:
        if not all([aluno.aluno_nome, aluno.aluno_cpf, aluno.aluno_email, aluno.fk_turma.turma]):
            alunos_campos_faltando.append(aluno)
    
    print(alunos_campos_faltando)
    return render(request, 'turma/lista.html', context)

@login_required
def sgc_turma_editar(request, id):
    context ={}
    turma_ob = get_object_or_404(Turma, id=id)
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=turma_ob)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Turma editada com sucesso.')
            return redirect('sgc_turma_lista')
    else:
        form = TurmaForm(instance=turma_ob)
    context = {
        'form': form,
        'turma_ob': turma_ob
    }
    return render(request, 'turma/editar.html', context)

@login_required
def sgc_turma_delete(request, id):
    context ={}
    turma_ob = get_object_or_404(Turma, id=id)
    if request.method == 'POST':
        turma_ob.delete()
        messages.add_message(request, messages.SUCCESS, 'Turma excluída com sucesso.')
        return redirect('sgc_turma_lista')
    
    context = {
        'turma_ob': turma_ob
    }
    
    return render(request, 'turma/excluir.html', context)