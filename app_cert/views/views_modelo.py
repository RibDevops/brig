from django.shortcuts import render, redirect, get_object_or_404
from ..models import Modelo
from ..forms import ModeloForm

def sgc_modelo_novo(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sgc_modelo_lista')  # Redirecione para a lista após criar
    else:
        form = ModeloForm()

    return render(request, 'modelo/criar.html', {'form': form})

def sgc_modelo_lista(request):
    dataset = Modelo.objects.select_related('fk_texto_modelo').all()
    for cert in dataset:
        print(cert.__dict__)
    context = {"dataset": dataset}
    return render(request, 'modelo/lista.html', context)

def sgc_modelo_editar(request, id):
    modelo_ob = get_object_or_404(Modelo, id=id)
    if request.method == 'POST':
        form = ModeloForm(request.POST, instance=modelo_ob)
        if form.is_valid():
            form.save()
            return redirect('sgc_modelo_lista')
    else:
        form = ModeloForm(instance=modelo_ob)
    context = {
        'form': form,
        'modelo_ob': modelo_ob
    }
    return render(request, 'modelo/editar.html', context)

def sgc_modelo_delete(request, id):
    modelo_ob = get_object_or_404(Modelo, id=id)
    if request.method == 'POST':
        modelo_ob.delete()
        return redirect('sgc_modelo_lista')

    context = {'modelo_ob': modelo_ob}
    return render(request, 'modelo/excluir.html', context)
