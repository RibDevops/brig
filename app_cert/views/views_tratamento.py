from django.shortcuts import render, redirect, get_object_or_404
from ..models import Tratamento
from ..forms import TratamentoForm
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.decorators import login_required


@login_required
def sgc_tratamento_novo(request):
    if request.method == 'POST':
        form = TratamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sgc_tratamento_lista')  # Redirecione para a lista após criar
    else:
        form = TratamentoForm()
    
    return render(request, 'tratamento/criar.html', {'form': form})

@login_required
def sgc_tratamento_lista(request):
    dataset = Tratamento.objects.all()
    context = {"dataset": dataset}
    # print(dataset)
    return render(request, 'tratamento/lista.html', context)

@login_required
def sgc_tratamento_editar(request, id):
    context ={}
    tratamento_ob = get_object_or_404(Tratamento, id=id)
    if request.method == 'POST':
        form = TratamentoForm(request.POST, instance=tratamento_ob)
        if form.is_valid():
            form.save()
            return redirect('sgc_tratamento_lista')
    else:
        form = TratamentoForm(instance=tratamento_ob)
    context = {
        'form': form,
        'tratamento_ob': tratamento_ob
    }
    return render(request, 'tratamento/editar.html', context)

@login_required
def sgc_tratamento_delete(request, id):
    context ={}
    tratamento_ob = get_object_or_404(Tratamento, id=id)
    if request.method == 'POST':
        tratamento_ob.delete()
        # messages.success(request, 'Registro excluído com sucesso.')
        return redirect('sgc_tratamento_lista')
    
    context = {
        'tratamento_ob': tratamento_ob
    }
    
    return render(request, 'tratamento/excluir.html', context)

