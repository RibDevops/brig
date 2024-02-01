
from django.shortcuts import render, redirect, get_object_or_404
from app_cert.models import Especialidade
from ..forms import EspecialidadeForm
from django.db.models import Count

# Create your views here.
def home(request):
    # context = gera_menu()  # Mescla o contexto existente com o novo contexto
    # return render(request, 'home.html', context )
    return render(request, 'sgu_home.html')

# def scp_espe_lista(request):
#     dataset = Especialidade.objects.all()
#     context = {"dataset": dataset}
#     # print(dataset)
#     return render(request, 'espe/lista.html', context)


def scp_espe_lista(request):
    # Consulta para obter todas as OM ordenadas por força/orgão
    dataset = (
        Especialidade.objects
        .values('fk_forca_orgao', 'fk_forca_orgao__forca_orgao' )  
            .annotate(total=Count('fk_forca_orgao'))  
            .prefetch_related('fk_forca_orgao')
        )
    
    print(dataset)
    context = {"dataset": dataset}
    return render(request, 'espe/lista.html', context)

def scp_espe_detalhes(request, id):
    # Obtém a instância da Especialidade com o ID fornecido ou retorna um erro 404 caso não exista
    # om = get_object_or_404(Especialidade, pk=id)

    # Filtra o conjunto de dados de Especialidade com base na OM específica
    dataset = Especialidade.objects.filter(fk_forca_orgao=id)

    context = {
        "dataset": dataset,
        # "om": om  # Passa a instância de Especialidade para o contexto
    }
    return render(request, 'espe/lista_espe.html', context)


def scp_espe_nova(request):
    if request.method == 'POST':
        form = EspecialidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scp_espe_lista')  # Redirecione para a lista após criar
    else:
        form = EspecialidadeForm()
    
    return render(request, 'espe/criar.html', {'form': form})

def scp_espe_ditar(request, id):
    context ={}
    espe_ob = get_object_or_404(Especialidade, id=id)
    if request.method == 'POST':
        form = EspecialidadeForm(request.POST, instance=espe_ob)
        if form.is_valid():
            form.save()
            return redirect('scp_espe_lista')
    else:
        form = EspecialidadeForm(instance=espe_ob)
    context = {
        'form': form,
        'espe_ob': espe_ob
    }
    return render(request, 'espe/editar.html', context)

def scp_espe_delete(request, id):
    context ={}
    espe_ob = get_object_or_404(Especialidade, id=id)
    if request.method == 'POST':
        espe_ob.delete()
        # messages.success(request, 'Registro excluído com sucesso.')
        return redirect('scp_espe_lista')
    
    context = {
        'espe_ob': espe_ob
    }
    
    return render(request, 'espe/excluir.html', context)


# def sgc_ano_detalhes(request, pk):
#     ano_ob = get_object_or_404(Especialidade, pk=pk)
#     return render(request, 'espe/detalhes.html', {'ano_ob': ano_ob})