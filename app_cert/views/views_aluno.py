from collections import Counter
import django.db.models
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from core.settings import STATIC_URL
from ..models import Aluno
from ..forms import AlunoForm
from django.shortcuts import get_object_or_404
import hashlib
import operator
import os
from core.settings import BASE_DIR
import os
import hashlib
import operator
from django.conf import settings
from django.http import JsonResponse
import qrcode
from django.http import JsonResponse
from ..models import Forca_Orgao, Posto, Quadro, Especialidade, Turma

from django.conf import settings
import os
from django.db.models import Count
from django.conf import settings
import os

from itertools import count, groupby


def sgc_generate_qr_code(data_gh, id):
    output_dir = os.path.join(settings.MEDIA_ROOT, 'qrcode')  # Caminho para a pasta 'media/qrcode'
    os.makedirs(output_dir, exist_ok=True)  # Cria o diretório se não existir

    filename = os.path.join('qrcode', '{}.png'.format(id)).replace('\\', '/')  # Salvar na pasta 'media' com a barra '/'
    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr_code.add_data('http://www.ciaer.intraer/certificado/valida.php?pesquisa=' + data_gh)
    qr_code.make(fit=True)
    image = qr_code.make_image(fill_color='black', back_color='white')

    image.save(os.path.join(settings.MEDIA_ROOT, filename))
    return filename

def sgc_generate_hash(data):
    sha256_hash = hashlib.sha256()
    
    # Obtenha o caminho absoluto para o arquivo 'key.key'
    file_path = os.path.join(os.path.dirname(__file__), 'key.key')

    # Abra o arquivo 'key.key' e leia a chave adicional
    with open(file_path, 'r') as file:
        lines = file.readlines()
        chave_adicional = ''.join(lines[1:-1]).strip()
    
    data_bytes = data.encode('utf-8')
    chave_bytes = chave_adicional.encode('utf-8')
    
    xor_result = bytes(map(operator.xor, data_bytes, chave_bytes))
    
    sha256_hash.update(xor_result)
    hash_value = sha256_hash.hexdigest()
    return hash_value[:15]

# def sgc_aluno_hash(id):
def sgc_aluno_hash(request, id):
    aluno_ob = get_object_or_404(Aluno, id=id)
    
    # Gerar o hash com base nas informações do aluno
    # aluno_info = f"{aluno_ob.aluno_nome} {aluno_ob.aluno_cpf}"
    aluno_info = f"{aluno_ob.aluno_nome} {aluno_ob.aluno_cpf} {aluno_ob.aluno_email} {aluno_ob.fk_turma.turma}"
    hash_aluno = sgc_generate_hash(aluno_info)

    qrcode = sgc_generate_qr_code(hash_aluno, id)

    print(hash_aluno)
    # Salvar o hash no modelo Aluno
    # Salvar o hash no modelo Aluno no campo 'codigo_hash'
    aluno_ob.codigo_hash = hash_aluno
    aluno_ob.qrcode = qrcode
    aluno_ob.save()
    
    # Redirecione de volta para a lista de alunos
    return redirect('sgc_aluno_lista')


# Esta parte precisa ser implementada em sua view.
def sgc_ajax_load_related_data_om(request):
    forca_orgao_id = request.GET.get('forca_orgao_id')

    postos = Posto.objects.filter(fk_forca_orgao_id=forca_orgao_id).all()
    quadros = Quadro.objects.filter(fk_forca_orgao_id=forca_orgao_id).all()
    especialidades = Especialidade.objects.filter(fk_forca_orgao_id=forca_orgao_id).all()

    postos_options = "<option value=''>---------</option>"
    quadros_options = "<option value=''>---------</option>"
    especialidades_options = "<option value=''>---------</option>"

    for posto in postos:
        postos_options += f"<option value='{posto.pk}'>{posto.posto}</option>"

    for quadro in quadros:
        quadros_options += f"<option value='{quadro.pk}'>{quadro.quadro}</option>"

    for especialidade in especialidades:
        especialidades_options += f"<option value='{especialidade.pk}'>{especialidade.especialidade}</option>"

    data = {
        'postos_options': postos_options,
        'quadros_options': quadros_options,
        'especialidades_options': especialidades_options
    }

    return JsonResponse(data)


def sgc_aluno_novo(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sgc_aluno_lista')  # Redirecione para a lista após criar
    else:
        form = AlunoForm()
    
    return render(request, 'aluno/criar.html', {'form': form})

# def sgc_aluno_lista(request):
#     dataset = Aluno.objects.all()
#     for aluno in dataset:
#         # Verifique se há um Certificado associado ao aluno
#         certificado = Certificado.objects.filter(fk_id_aluno=aluno).first()
#         aluno.has_certificado = bool(certificado)  # Define um atributo personalizado
#     context = {"dataset": dataset}
#     for aluno in dataset:
#         print(aluno.__dict__)
#     return render(request, 'aluno/lista.html', context)dataset = Aluno.objects.select_related('fk_id_aluno').all()

# def sgc_aluno_lista(request):
#     # Obtém todos os alunos
#     dataset = Aluno.objects.all()

#     # Crie o contexto com a lista de alunos e se eles têm certificado
#     context = {
#         "dataset": dataset,
#         # "alunos_com_certificado": Certificado.objects.values_list('fk_id_aluno_id', flat=True)
#     }
    
#     return render(request, 'aluno/lista.html', context)

def sgc_aluno_lista(request):
    # Obtém todos os alunos
    dataset = (
        Aluno.objects
        .values('fk_turma', 'fk_turma__turma_sgc')  # Adiciona o campo 'fk_turma__turma' para pegar a descrição da turma
        .annotate(total=Count('id'))  # Anotação para contar o número de ocorrências de cada valor de fk_turma
        .prefetch_related('fk_turma')  # Carrega os objetos relacionados usando prefetch_related
    )
    print(dataset)
    context = {"dataset": dataset}
    return render(request, 'aluno/lista_turma.html', context)

def sgc_aluno_lista_detalhes(request, id):
    print(id)
    # Filtra o conjunto de dados de Aluno com base na turma específica
    dataset = Aluno.objects.filter(fk_turma=id)
    # print(alunos_turma)

    context = {
        "dataset": dataset,
        # "turma_sgc": turma_sgc
    }
    return render(request, 'aluno/lista.html', context)

# def sgc_aluno_detalhes(request, pk):
#     aluno_ob = get_object_or_404(AlunoForm, pk=pk)
#     return render(request, 'aluno/detalhes.html', {'aluno_ob': aluno_ob})

def sgc_aluno_editar(request, id):
    context ={}
    aluno_ob = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno_ob)
        if form.is_valid():
            form.save()
            return redirect('sgc_aluno_lista')
    else:
        form = AlunoForm(instance=aluno_ob)
    context = {
        'form': form,
        'aluno_ob': aluno_ob
    }
    return render(request, 'aluno/editar.html', context)

def sgc_aluno_delete(request, id):
    context ={}
    aluno_ob = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        aluno_ob.delete()
        # messages.success(request, 'Registro excluído com sucesso.')
        return redirect('sgc_aluno_lista')
    
    context = {
        'aluno_ob': aluno_ob
    }
    
    return render(request, 'aluno/excluir.html', context)

