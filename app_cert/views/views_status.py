from django.shortcuts import render, redirect, get_object_or_404
from ..models import Status
from ..forms import StatusForm


def status_nova(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status_lista')  # Redirecione para a lista após criar
    else:
        form = StatusForm()
    
    return render(request, 'status/criar.html', {'form': form})

def status_lista(request):
    dataset = Status.objects.all()
    context = {"dataset": dataset}
    # print(dataset)
    return render(request, 'status/lista.html', context)


# def status_detalhes(request, pk):
#     status_ob = get_object_or_404(StatusForm, pk=pk)
#     return render(request, 'status/detalhes.html', {'status_ob': status_ob})

def status_editar(request, id):
    context ={}
    status_ob = get_object_or_404(Status, id=id)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status_ob)
        if form.is_valid():
            form.save()
            return redirect('status_lista')
    else:
        form = StatusForm(instance=status_ob)
    context = {
        'form': form,
        'status_ob': status_ob
    }
    return render(request, 'status/editar.html', context)

def status_delete(request, id):
    context ={}
    status_ob = get_object_or_404(Status, id=id)
    if request.method == 'POST':
        status_ob.delete()
        # messages.success(request, 'Registro excluído com sucesso.')
        return redirect('status_lista')
    
    context = {
        'status_ob': status_ob
    }
    
    return render(request, 'status/excluir.html', context)

