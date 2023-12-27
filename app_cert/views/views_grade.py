from django.shortcuts import render, redirect, get_object_or_404
from app_cert.models import In_Ex
from ..models import GradeTurma, Instrucao, Turma
from ..forms import GradeTurmaForm # Importe o formulário adequado
from django.db.models import F
from django.db.models import Count


def sgc_home(request):
    return render(request, 'sgc_home.html')

def sgc_grade_nova(request):
    if request.method == 'POST':
        print(request.POST)
        post_p = request.POST

        print(f'posto da pagina: {post_p}')
        form = GradeTurmaForm(request.POST)
        if form.is_valid():
              
            form.save()
            return redirect('sgc_grade_lista')  # Redirecione para a lista após criar
    else:
        form = GradeTurmaForm()
        dataset = {
            'instrucoes': Instrucao.objects.values('id', 'instrucao_descricao'),
            'in_ex': In_Ex.objects.values('id', 'in_ex'),
            'form': form
           
        }
    return render(request, 'grade/criar.html', dataset)

def sgc_grade_lista(request):
    dataset = (
        GradeTurma.objects
        .values('fk_turma', 'fk_turma__turma')  # Adiciona o campo 'fk_turma__turma' para pegar a descrição da turma
        .annotate(total=Count('fk_turma'))  # Anotação para contar o número de ocorrências de cada valor de fk_turma
        .prefetch_related('fk_turma')  # Carrega os objetos relacionados usando prefetch_related
    )
    context = {"dataset": dataset}
    return render(request, 'grade/lista.html', context)


def sgc_grade_detalhes(request, turma_id):
    # Obtém a instância da Turma com o ID fornecido ou retorna um erro 404 caso não exista
    turma = get_object_or_404(Turma, id=turma_id)

    # Filtra o conjunto de dados de GradeTurma com base na turma específica
    dataset = GradeTurma.objects.filter(fk_turma=turma)

    context = {
        "dataset": dataset,
        "turma": turma  # Passa a instância de turma para o contexto
    }
    # return render(request, 'grade/lista.html', context)
    return render(request, 'grade/lista_grade_turma.html', context)


# def sgc_grade_lista(request):
#     # dataset = GradeTurma.objects.select_related('fk_turma', 'fk_in_ex', ).all()
#     dataset = GradeTurma.objects.all().distinct('fk_turma')
#     context = {"dataset": dataset}
#     print(dataset)
#     return render(request, 'grade/lista.html', context)

# def sgc_grade_lista(request):
#     # Obtendo valores únicos para fk_turma
#     unique_fk_turma_ids = GradeTurma.objects.values('fk_turma').distinct()

#     # Filtrando os registros com base nos valores únicos de fk_turma
#     dataset = GradeTurma.objects.filter(pk__in=[obj['fk_turma'] for obj in unique_fk_turma_ids])

#     context = {"dataset": dataset}
#     print(dataset)
#     return render(request, 'grade/lista.html', context)




# def sgc_grade_lista(request):
#     dataset = (
#         GradeTurma.objects
#         .values('fk_turma', 'fk_in_ex')  # Seleciona as colunas desejadas para o distinct
#         .annotate(
#             id=F('id'),
#             fk_instrucao=F('fk_instrucao_id'),
#             tempo_instrucao=F('tempo_instrucao')
#         )
#         .distinct()  # Aplica o distinct nessas colunas
#     )
#     context = {"dataset": dataset}
#     print(dataset)
#     return render(request, 'grade/lista.html', context)

def sgc_grade_editar(request, id):
    context ={}
    grade_ob = get_object_or_404(GradeTurma, id=id)
    if request.method == 'POST':
        form = GradeTurmaForm(request.POST, instance=grade_ob)
        if form.is_valid():
            form.save()
            return redirect('sgc_grade_lista')
    else:
        form = GradeTurmaForm(instance=grade_ob)
    context = {
        'form': form,
        'grade_ob': grade_ob
    }
    return render(request, 'grade/editar.html', context)

def sgc_grade_delete(request, id):
    context ={}
    grade_ob = get_object_or_404(GradeTurma, id=id)
    if request.method == 'POST':
        grade_ob.delete()
        # messages.success(request, 'Registro excluído com sucesso.')
        return redirect('sgc_grade_lista')
    
    context = {
        'grade_ob': grade_ob
    }
    
    return render(request, 'grade/excluir.html', context)

