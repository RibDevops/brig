from django.shortcuts import render, redirect, get_object_or_404
from ..models import Imagem
from ..forms import ImagemForm

def sgc_imagem_nova(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sgc_imagem_lista')  # Redirecione para a lista após criar
    else:
        form = ImagemForm()
    
    return render(request, 'imagem/criar.html', {'form': form})

def sgc_imagem_lista(request):
    dataset = Imagem.objects.all()
    context = {"dataset": dataset}
    for imagem in dataset:
        print(imagem.__dict__)
    return render(request, 'imagem/lista.html', context)

# def sgc_assinatura_detalhes(request, pk):
#     assinatura_ob = get_object_or_404(AssinaturaForm, pk=pk)
#     return render(request, 'imagem/detalhes.html', {'assinatura_ob': assinatura_ob})

def sgc_imagem_editar(request, id):
    context ={}
    assinatura_ob = get_object_or_404(Imagem, id=id)
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES, instance=assinatura_ob)
        if form.is_valid():
            form.save()
            return redirect('sgc_imagem_lista')
    else:
        form = ImagemForm(instance=assinatura_ob)
    context = {
        'form': form,
        'assinatura_ob': assinatura_ob
    }
    return render(request, 'imagem/editar.html', context)

def sgc_imagem_delete(request, id):
    context ={}
    assinatura_ob = get_object_or_404(Imagem, id=id)
    if request.method == 'POST':
        assinatura_ob.delete()
        # messages.success(request, 'Registro excluído com sucesso.')
        return redirect('sgc_imagem_lista')
    
    context = {
        'assinatura_ob': assinatura_ob
    }
    
    return render(request, 'imagem/excluir.html', context)

