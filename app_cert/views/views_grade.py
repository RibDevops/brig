from django.shortcuts import render, redirect, get_object_or_404
from app_cert.models import In_Ex
from ..models import GradeTurma, Instrucao, Turma
from ..forms import GradeTurmaForm # Importe o formulário adequado
from django.db.models import F
from django.db.models import Count
from django.contrib import messages
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.decorators import login_required


@login_required
def sgc_grade_nova(request):
    if request.method == 'POST':
        print(request.POST)
        post_data = request.POST

        print(f'posto da pagina: {post_data}')

        fk_turma_list = post_data.getlist('fk_turma')
        print(f'fk_turma - {fk_turma_list}')

        # Coleta os dados de inst_x presentes no POST
        grade_data_list = []
        for key, value in post_data.items():
            if key.startswith('inst_'):
                inst_num = key.split('_')[1]
                inst_value = value[0] if isinstance(value, list) else value  # Lida com a lista de valores
                int_value = int(post_data.get(f'int_{inst_num}', 0))
                ext_value = int(post_data.get(f'ext_{inst_num}', 0))
                tempo_value = int(post_data.get(f'tempo_{inst_num}', 0))

                grade_data = {
                    'fk_turma': fk_turma_list[0],
                    'fk_instrucao': inst_value,
                    'interno': int_value,
                    'externo': ext_value,
                    'tempo_instrucao': tempo_value
                }
                grade_data_list.append(grade_data)
                print(f'Grade Data {inst_num}: {grade_data}')

                # Insira o código para salvar cada conjunto de dados no banco de dados
                # ...

        forms = [GradeTurmaForm(data) for data in grade_data_list]

        if all(form.is_valid() for form in forms):
            for form in forms:
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Grade cadastrada com sucesso.')
        else:
            print(f'Pelo menos um formulário é inválido')

        return redirect('sgc_grade_lista')
    else:
        form = GradeTurmaForm()
        dataset = {
            'instrucoes': Instrucao.objects.values('id', 'instrucao_descricao', 'instrucao_sigla'),
            'in_ex': In_Ex.objects.values('id', 'in_ex'),
            'form': form
        }
        return render(request, 'grade/criar.html', dataset)

@login_required
def sgc_grade_lista(request):
    dataset = (
        GradeTurma.objects
        .values('fk_turma', 'fk_turma__turma_sgc')  # Adiciona o campo 'fk_turma__turma' para pegar a descrição da turma
        .annotate(total=Count('fk_turma'))  # Anotação para contar o número de ocorrências de cada valor de fk_turma
        .prefetch_related('fk_turma')  # Carrega os objetos relacionados usando prefetch_related
    )
    context = {"dataset": dataset}
    return render(request, 'grade/lista.html', context)

@login_required
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

@login_required
def sgc_grade_editar(request, id):
    context ={}
    grade_ob = get_object_or_404(GradeTurma, id=id)
    if request.method == 'POST':
        form = GradeTurmaForm(request.POST, instance=grade_ob)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Grade editada com sucesso.')
            return redirect('sgc_grade_lista')
    else:
        form = GradeTurmaForm(instance=grade_ob)
    context = {
        'form': form,
        'grade_ob': grade_ob
    }
    return render(request, 'grade/editar.html', context)

@login_required
def sgc_grade_delete(request, id):
    context ={}
    grade_ob = get_object_or_404(GradeTurma, id=id)
    if request.method == 'POST':
        grade_ob.delete()
        messages.add_message(request, messages.SUCCESS, 'Grade excluída com sucesso.')

        # messages.success(request, 'Registro excluído com sucesso.')
        return redirect('sgc_grade_lista')
    
    context = {
        'grade_ob': grade_ob
    }
    
    return render(request, 'grade/excluir.html', context)

