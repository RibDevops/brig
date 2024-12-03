import csv
import io
import os
from django.conf import settings
import nltk
from nltk.corpus import names
from django.shortcuts import render
from ..forms import CSVUploadForm
from ..models import Aluno, Posto, Quadro, Especialidade, Om, Tratamento, Turma
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.decorators import login_required



# Baixe o corpus de nomes se ainda não tiver feito isso
nltk.download('names')

def ler_nomes_do_arquivo(arquivo):
    caminho_completo = os.path.join(settings.BASE_DIR, 'static', 'txt', arquivo)
    with open(caminho_completo, "r", encoding="utf-8") as file:
        nomes = [nome.strip().lower() for nome in file.readlines()]
    return nomes

def identificar_genero(nome, nomes_masculinos, nomes_femininos):
    primeiro_nome = nome.strip().split()[0].capitalize()

    if primeiro_nome.lower() in nomes_masculinos:
        return "1"
    elif primeiro_nome.lower() in nomes_femininos:
        return "2"
    else:
        return "1"

@login_required
def sgc_import_csv_view(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Carregar listas de nomes masculinos e femininos
            meus_nomes_masculinos = ler_nomes_do_arquivo("nomes_masculinos.txt")
            meus_nomes_femininos = ler_nomes_do_arquivo("nomes_femininos.txt")

            csvfile = request.FILES['file']
            data_set = csvfile.read().decode('utf-8')
            io_string = io.StringIO(data_set)
            next(io_string)  # Ignora o cabeçalho, se houver

            for row in csv.reader(io_string, delimiter='|'):
                turma, posto, quadro, especialidade, nome_completo, om_nome, cpf, email = row[1], row[2], row[3], row[4], row[5], row[7], row[9], row[14]

                # Identificar gênero
                genero = identificar_genero(nome_completo, meus_nomes_masculinos, meus_nomes_femininos)
                print(f'tratamento {genero}')

                # Buscar chaves estrangeiras
                # turma_obj = Turma.objects.get_or_create(turma=turma)[0]
                # posto_obj = Posto.objects.get_or_create(posto=posto)[0]
                # quadro_obj = Quadro.objects.get_or_create(quadro=quadro)[0]
                # especialidade_obj = Especialidade.objects.get_or_create(especialidade=especialidade)[0]
                # om_obj = Om.objects.get_or_create(om=om_nome)[0]
                tratamento = Tratamento.objects.get(pk=int(genero)) 
                # turma_obj = Tratamento.objects.filter(turma=turma).first()
                turma_obj = Turma.objects.filter(turma_sgc=turma).first()
                posto_obj = Posto.objects.filter(posto=posto).first()
                quadro_obj = Quadro.objects.filter(quadro=quadro).first()
                especialidade_obj = Especialidade.objects.filter(especialidade=especialidade).first()
                om_obj = Om.objects.filter(om=om_nome).first()

                # Criar objeto Aluno com chaves estrangeiras
                aluno = Aluno.objects.create(
                    aluno_nome=nome_completo,
                    fk_tratamento=tratamento,
                    aluno_cpf=cpf,
                    aluno_email=email,
                    fk_posto=posto_obj,
                    fk_quadro=quadro_obj,
                    fk_especialidade=especialidade_obj,
                    fk_om=om_obj,
                    fk_turma=turma_obj,
                )

            return render(request, 'csv/sucesso.html')
    else:
        form = CSVUploadForm()
    return render(request, 'csv/import.html', {'form': form})
