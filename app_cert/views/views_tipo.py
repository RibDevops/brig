from django.shortcuts import render, redirect, get_object_or_404
from ..models import Tipo
from ..forms import TipoForm
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.decorators import login_required


@login_required
def sgc_tipo_novo(request):
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sgc_tipo_lista')  # Redirecione para a lista após criar
    else:
        form = TipoForm()
    
    return render(request, 'tipo/criar.html', {'form': form})

@login_required
def sgc_tipo_lista(request):
    dataset = Tipo.objects.all()
    context = {"dataset": dataset}
    # print(dataset)
    return render(request, 'tipo/lista.html', context)

@login_required
def sgc_tipo_editar(request, id):
    context ={}
    tipo_ob = get_object_or_404(Tipo, id=id)
    if request.method == 'POST':
        form = TipoForm(request.POST, instance=tipo_ob)
        if form.is_valid():
            form.save()
            return redirect('sgc_tipo_lista')
    else:
        form = TipoForm(instance=tipo_ob)
    context = {
        'form': form,
        'tipo_ob': tipo_ob
    }
    return render(request, 'tipo/editar.html', context)

@login_required
def sgc_tipo_delete(request, id):
    context ={}
    tipo_ob = get_object_or_404(Tipo, id=id)
    if request.method == 'POST':
        tipo_ob.delete()
        # messages.success(request, 'Registro excluído com sucesso.')
        return redirect('sgc_tipo_lista')
    
    context = {
        'tipo_ob': tipo_ob
    }
    
    return render(request, 'tipo/excluir.html', context)

