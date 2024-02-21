from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from requests import request
from app_cert.models import Curso
from app_cert.forms import CursoForm  # Importe o formulário adequado
from django.contrib import messages
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.decorators import has_permission_decorator



@has_permission_decorator('novo')
def sgc_curso_novo(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Curso cadastrado com sucesso.')
            return redirect('sgc_curso_lista')  # Redirecione para a lista após criar
    else:
        form = CursoForm()
    
    return render(request, 'curso/criar.html', {'form': form})

@has_permission_decorator('lista')
def sgc_curso_lista(request):
    dataset = Curso.objects.all()
    context = {"dataset": dataset}
    # for curso in dataset:
    #     print(curso.__dict__)
    
    # for curso in dataset:
    #     assinaturas = curso.fk_assinaturas
    #     if assinaturas:
    #         print("Curso:", curso.curso)
    #         print("Esquerda:", assinaturas.esquerda)
    #         print("Esquerda Cargo:", assinaturas.esquerda_cargo)
    #         print("Direita:", assinaturas.direita)
    #         print("Direita Cargo:", assinaturas.direita_cargo)
    #         print("\n")
    return render(request, 'curso/lista.html', context)

@has_permission_decorator('editar')
def sgc_curso_editar(request, id):
    context ={}
    curso_ob = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso_ob)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Curso editado com sucesso.')
            return redirect('sgc_curso_lista')
    else:
        form = CursoForm(instance=curso_ob)
    context = {
        'form': form,
        'curso_ob': curso_ob
    }
    return render(request, 'curso/editar.html', context)

@has_permission_decorator('excluir')
def sgc_curso_delete(request, id):
    context ={}
    curso_ob = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso_ob.delete()
        messages.add_message(request, messages.SUCCESS, 'Curso excluído com sucesso.') 
        return redirect('sgc_curso_lista')
    
    context = {
        'curso_ob': curso_ob
    }
    
    return render(request, 'curso/excluir.html', context)

