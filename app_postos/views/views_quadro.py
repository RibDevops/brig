
from django.shortcuts import render, redirect, get_object_or_404
from app_cert.models import Quadro
from ..forms import QuadroForm
from django.db.models import Count
from django.contrib import messages

# Create your views here.
def home(request):
    # context = gera_menu()  # Mescla o contexto existente com o novo contexto
    # return render(request, 'home.html', context )
    return render(request, 'sgu_home.html')

# def scp_quadro_lista(request):
#     dataset = Quadro.objects.all()
#     context = {"dataset": dataset}
#     # print(dataset)
#     return render(request, 'omlista.html', context)


def scp_quadro_lista(request):
    # Consulta para obter todas as OM ordenadas por força/orgão
    dataset = (
        Quadro.objects
        .values('fk_forca_orgao', 'fk_forca_orgao__forca_orgao' )  
            .annotate(total=Count('fk_forca_orgao'))  
            .prefetch_related('fk_forca_orgao')
        )
    
    print(dataset)
    context = {"dataset": dataset}
    return render(request, 'omlista.html', context)

def scp_quadro_detalhes(request, id):
    # Obtém a instância da Quadro com o ID fornecido ou retorna um erro 404 caso não exista
    # om = get_object_or_404(Quadro, pk=id)

    # Filtra o conjunto de dados de Quadro com base na OM específica
    dataset = Quadro.objects.filter(fk_forca_orgao=id)

    context = {
        "dataset": dataset,
        # "om": om  # Passa a instância de Quadro para o contexto
    }
    return render(request, 'omlista_om.html', context)


def scp_quadro_novo(request):
    if request.method == 'POST':
        form = QuadroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Quadro cadastrado com sucesso.')
            return redirect('scp_quadro_lista')  # Redirecione para a lista após criar
    else:
        form = QuadroForm()
    
    return render(request, 'omcriar.html', {'form': form})

def scp_quadro_ditar(request, id):
    context ={}
    om_ob = get_object_or_404(Quadro, id=id)
    if request.method == 'POST':
        form = QuadroForm(request.POST, instance=om_ob)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Quadro editado com sucesso.')
            return redirect('scp_quadro_lista')
    else:
        form = QuadroForm(instance=om_ob)
    context = {
        'form': form,
        'om_ob': om_ob
    }
    return render(request, 'omeditar.html', context)

def scp_quadro_delete(request, id):
    context ={}
    om_ob = get_object_or_404(Quadro, id=id)
    if request.method == 'POST':
        om_ob.delete()
        messages.add_message(request, messages.SUCCESS, 'Quadro excluído com sucesso.') 
        return redirect('scp_quadro_lista')
    
    context = {
        'om_ob': om_ob
    }
    
    return render(request, 'omexcluir.html', context)


# def sgc_ano_detalhes(request, pk):
#     ano_ob = get_object_or_404(Quadro, pk=pk)
#     return render(request, 'omdetalhes.html', {'ano_ob': ano_ob})
