# # import csv
# # import io

# # from django.shortcuts import render
# # from ..forms import CSVUploadForm
# # from ..models import Aluno

# # def sgc_import_csv_view(request):
# #     if request.method == 'POST':
# #         form = CSVUploadForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             csvfile = request.FILES['file']
# #             # data_set = csvfile.read().decode('UTF-8')
# #             data_set = csvfile.read().decode('latin-1')
# #             # data_set = csvfile.read().decode('ISO-8859-1')
# #             io_string = io.StringIO(data_set)
# #             next(io_string)  # Ignora o cabeçalho, se houver
# #             for row in csv.reader(io_string, delimiter=':', quotechar="|"):
# #                 _, created = Aluno.objects.update_or_create(
# #                     aluno_nome=row[0],
# #                     aluno_cpf=row[1],
# #                     aluno_email=row[2]
# #                 )
# #             return render(request, 'csv/sucesso.html')
# #     else:
# #         form = CSVUploadForm()
# #     return render(request, 'csv/import.html', {'form': form})

# #     alterar def sgc_para fazer import do arquivo csv com os campos abaixo:

# #     TIPO INDC.|TURMA|POSTO/GRAD.|QUADRO|ESP.|NOME COMPLETO|NOME GUERRA|OM|IDENTIDADE|CPF|SARAM|DT. NASC.|DT. PRAÇA|DT. ÚLTIMA APRES.|E-MAIL|TELEFONE|STATUS INDC.|PAI|MÃE|CREDENCIAL DE SEG.|CUSTO ESTIM. PASSAGENS|CUSTO ESTIM. DIÁRIAS|CUSTO ESTIM. AJD. CUSTO|FUNÇÃO ATUAL|TEMPO ATIVIDADE|FUNÇÃO APÓS CURSO|ATENDE PRÉ-REQUISITO|JUSTIFICATIVA|PLANO TRANSMIS. CONHEC.|CURSOS NA ÁREA|QTD. COM CURSO NA OM|QTD. COM CURSO NO ELO|QTD. MÍNIMA NO ELO|QTD. IDEAL NO ELO|OBSERVAÇÃO|PRIORIDADE|INDC. REALIZADA POR|OM BENEFICIADA|DT. INDC.|CHEFE|E-MAIL CHEFE|TEL. CHEFE|TEL. OM|COORD. LOCAL|E-MAIL COORD. LOCAL|TEL. COORD. LOCAL

# #     os campos que serao aproveitados são os compos abaixo:
# #     TURMA|POSTO/GRAD.|QUADRO|ESP.|NOME COMPLETO|OM|IDENTIDADE|CPF|E-MAIL

# #     nesses campos abaixo sera feito uma pesquisa para pegar a pk
# #     POSTO/GRAD.|QUADRO|ESP.|OM|

# #     exemplo pesquisa com a informação do campo POSTO/GRAD.:
# #     POSTO/GRAD. = 'MA'

# #         select app_cert.Posto
# #             if POSTO/GRAD. = app_cert.Posto
# #                 POSTO/GRAD. = "pk": "1",
# #             else
# #                 POSTO/GRAD. = 0
    
# #     repetir a pesquisa para os campo: 
    
# #     if POSTO/GRAD. = app_cert.Posto
# #     if QUADRO = app_cert.Quadro
# #     if ESP. = app_cert.Especialidade
# #     if OM = app_cert.Om

# #     {
# #       "model": "app_cert.Posto",
# #       "pk": "1",
# #       "fields": {
# #         "fk_forca_orgao": "1",
# #         "hierarquia": "1",
# #         "posto": "MA",
# #         "posto_descricao": "Marechal do Ar"
# #       }
# #     },

# #     {
# #       "model": "app_cert.Quadro",
# #       "pk": "2",
# #       "fields": {
# #         "fk_forca_orgao": "1",
# #         "quadro": "QOINT",
# #         "quadro_descricao": "QOINT"
# #       }
# #     },
# #     {
# #       "model": "app_cert.Especialidade",
# #       "pk": "1",
# #       "fields": {
# #         "fk_forca_orgao": "1",
# #         "especialidade": "ADE",
# #         "especialidade_descricao": "ADE"
# #       }
# #     },

# #     {
# #       "model": "app_cert.Om",
# #       "pk": "1",
# #       "fields": {
# #         "fk_forca_orgao": "1",
# #         "om": "I COMAR",
# #         "om_descricao": "I COMAR"
# #       }
# #     },

# import io
# from django.shortcuts import render
# import csv
# from ..forms import CSVUploadForm
# from ..models import Aluno, Posto, Quadro, Especialidade, Om, Turma

# # def sgc_import_csv_view(request):
# #     if request.method == 'POST':
# #         form = CSVUploadForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             csvfile = request.FILES['file']
# #             data_set = csvfile.read().decode('latin-1')
# #             io_string = io.StringIO(data_set)
# #             next(io_string)  # Ignora o cabeçalho, se houver
# #             for row in csv.reader(io_string, delimiter='|'):
# #                 # Mapear os índices dos campos do CSV para os campos desejados
# #                 turma, posto_grad, quadro, esp, nome_completo, om, identidade, cpf, email = row[:9]

# #                 # Realizar a busca pelos objetos correspondentes nos modelos Django
# #                 try:
# #                     turma = Turma.objects.get(turma=turma)
# #                     posto_obj = Posto.objects.get(posto=posto_grad)
# #                     quadro_obj = Quadro.objects.get(quadro=quadro)
# #                     esp_obj = Especialidade.objects.get(especialidade=esp)
# #                     om_obj = Om.objects.get(om=om)

# #                     # Criação ou atualização do objeto Aluno associado aos objetos encontrados
# #                     aluno, created = Aluno.objects.update_or_create(
# #                         aluno_nome=nome_completo,
# #                         aluno_cpf=cpf,
# #                         aluno_email=email,
# #                         fk_posto=posto_obj,
# #                         fk_quadro=quadro_obj,
# #                         fk_especialidade=esp_obj,
# #                         fk_om=om_obj
# #                     )
# #                 except (Posto.DoesNotExist, Quadro.DoesNotExist, Especialidade.DoesNotExist, Om.DoesNotExist, Turma.DoesNotExist):
# #                     # Lidar com casos em que não são encontrados objetos correspondentes
# #                     # Pode ser tratado conforme necessário
# #                     pass

# #             return render(request, 'csv/sucesso.html')
# #     else:
# #         form = CSVUploadForm()
# #     return render(request, 'csv/import.html', {'form': form})
# from django.shortcuts import render
# from ..forms import CSVUploadForm
# from ..models import Aluno, Posto, Quadro, Especialidade, Om, Turma

# import nltk
# from nltk.corpus import names

# # Baixe o corpus de nomes se ainda não tiver feito isso
# nltk.download('names')

# def ler_nomes_do_arquivo(arquivo):
#     with open(arquivo, "r", encoding="utf-8") as file:
#         nomes = [nome.strip().lower() for nome in file.readlines()]
#     return nomes

# def identificar_genero(nome, nomes_masculinos, nomes_femininos):
#     primeiro_nome = nome.strip().split()[0].capitalize()

#     if primeiro_nome.lower() in nomes_masculinos:
#         return "1"
#     elif primeiro_nome.lower() in nomes_femininos:
#         return "2"
#     else:
#         return "0"

# def main(nome):
#     # Lista de nomes masculinos personalizados
#     meus_nomes_masculinos = ler_nomes_do_arquivo("nomes_masculinos.txt")

#     # Lista de nomes femininos personalizados
#     meus_nomes_femininos = ler_nomes_do_arquivo("nomes_femininos.txt")

#     # Identificar gênero para o nome fornecido
#     genero = identificar_genero(nome, meus_nomes_masculinos, meus_nomes_femininos)
    
#     if genero != "desconhecido":
#         print(f"Gênero do nome '{nome}': {genero}")
#     else:
#         print(f"Gênero do nome '{nome}': desconhecido")

# # Substitua "nome_a_identificar" pelo nome que deseja classificar
# if __name__ == "__main__":
#     main("nome_a_identificar")


# def sgc_import_csv_view(request):
#     if request.method == 'POST':
#         form = CSVUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             csvfile = request.FILES['file']
#             data_set = csvfile.read().decode('latin-1')
#             io_string = io.StringIO(data_set)
#             next(io_string)  # Ignora o cabeçalho, se houver
#             for row in csv.reader(io_string, delimiter='|'):  # Altere o delimitador conforme seu arquivo
#                 turma = row[1]
#                 posto = row[2]
#                 quadro = row[3]
#                 especialidade = row[4]
#                 nome_completo = row[5]
#                 om_nome = row[7]
#                 # identidade = row[6]
#                 cpf = row[9]
#                 email = row[14]

#                 # Identificar gênero
#                 genero = identificar_genero(nome_completo)

#                 # Encontrar chaves estrangeiras
#                 turma_obj = Turma.objects.filter(turma=turma).first()
#                 posto_obj = Posto.objects.filter(posto=posto).first()
#                 quadro_obj = Quadro.objects.filter(quadro=quadro).first()
#                 especialidade_obj = Especialidade.objects.filter(especialidade=especialidade).first()
#                 om_obj = Om.objects.filter(om=om_nome).first()

#                 # Criação do objeto Aluno com chaves estrangeiras
#                 aluno = Aluno.objects.create(
#                     aluno_nome = nome_completo,
#                     fk_tratamento = genero,
#                     aluno_cpf = cpf,
#                     aluno_email = email,
#                     # identidade=identidade,
#                     fk_posto = posto_obj,
#                     fk_quadro = quadro_obj,
#                     fk_especialidade = especialidade_obj,
#                     fk_om = om_obj,
#                     fk_turma = turma_obj,
#                 )

#             return render(request, 'csv/sucesso.html')
#     else:
#         form = CSVUploadForm()
#     return render(request, 'csv/import.html', {'form': form})

import csv
import io
import os
from django.conf import settings
import nltk
from nltk.corpus import names

from django.shortcuts import render
from ..forms import CSVUploadForm
from ..models import Aluno, Posto, Quadro, Especialidade, Om, Tratamento, Turma

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
