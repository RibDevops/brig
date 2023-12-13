from django.shortcuts import render, redirect, get_object_or_404
from ..models import GradeTurma
from ..forms import GradeTurmaForm # Importe o formulário adequado


def home(request):
    return render(request, 'home.html')

def grade_nova(request):
    if request.method == 'POST':
        form = GradeTurmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_lista')  # Redirecione para a lista após criar
    else:
        form = GradeTurmaForm()
    
    return render(request, 'grade/criar.html', {'form': form})

def grade_lista(request):
    dataset = GradeTurma.objects.select_related('fk_turma', 'fk_in_ex', ).all()
    context = {"dataset": dataset}
    print(dataset)
    return render(request, 'grade/lista.html', context)

def grade_editar(request, id):
    context ={}
    grade_ob = get_object_or_404(GradeTurma, id=id)
    if request.method == 'POST':
        form = GradeTurmaForm(request.POST, instance=grade_ob)
        if form.is_valid():
            form.save()
            return redirect('grade_lista')
    else:
        form = GradeTurmaForm(instance=grade_ob)
    context = {
        'form': form,
        'grade_ob': grade_ob
    }
    return render(request, 'grade/editar.html', context)

def grade_delete(request, id):
    context ={}
    grade_ob = get_object_or_404(GradeTurma, id=id)
    if request.method == 'POST':
        grade_ob.delete()
        # messages.success(request, 'Registro excluído com sucesso.')
        return redirect('grade_lista')
    
    context = {
        'grade_ob': grade_ob
    }
    
    return render(request, 'grade/excluir.html', context)

