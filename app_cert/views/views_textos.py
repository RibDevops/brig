from django.shortcuts import render, redirect, get_object_or_404
from ..models import Textos
from ..forms import TextoForm
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('novo')
def sgc_texto_novo(request):
    if request.method == 'POST':
        form = TextoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sgc_texto_lista')  # Redirecione para a lista após criar
    else:
        form = TextoForm()
    
    return render(request, 'texto/criar.html', {'form': form})

@has_permission_decorator('lista')
def sgc_texto_lista(request):
    dataset = Textos.objects.all()
    # dataset = Textos.objects.select_related(
    #     'fk_curso',
    #     'fk_tipo'
    #     ).all()
    context = {"dataset": dataset}
    # print(dataset)
    return render(request, 'texto/lista.html', context)

@has_permission_decorator('editar')
def sgc_texto_editar(request, id):
    context ={}
    texto_ob = get_object_or_404(Textos, id=id)
    if request.method == 'POST':
        form = TextoForm(request.POST, instance=texto_ob)
        if form.is_valid():
            form.save()
            return redirect('sgc_texto_lista')
    else:
        form = TextoForm(instance=texto_ob)
    context = {
        'form': form,
        'texto_ob': texto_ob
    }
    return render(request, 'texto/editar.html', context)

@has_permission_decorator('excluir')
def sgc_texto_delete(request, id):
    context ={}
    texto_ob = get_object_or_404(Textos, id=id)
    if request.method == 'POST':
        texto_ob.delete()
        # messages.success(request, 'Registro excluído com sucesso.')
        return redirect('sgc_texto_lista')
    
    context = {
        'texto_ob': texto_ob
    }
    
    return render(request, 'texto/excluir.html', context)

