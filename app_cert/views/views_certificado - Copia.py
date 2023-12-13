import zipfile
from django import template
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from ..utils import *
from ..models import *
from ..forms import *
from django.db.models import Count
from django.template import RequestContext
import io
from django.core.files.storage import FileSystemStorage
import django.http
from django.template.loader import render_to_string
from django.views.generic import View
from reportlab.pdfgen import canvas
from django.views.generic import View
# from ..utils import PDFGenerator
from app_cert.models import Modelo  # Importe seus modelos aqui

from django.shortcuts import render
# from products.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.staticfiles import finders
from datetime import datetime
from PyPDF2 import PdfMerger
from django.db.models import Q  # Adicione esta linha para importar o módulo Q

from django.shortcuts import render
from django.db.models import Q
from collections import defaultdict
from ..models import Turma, Aluno
from django.http import HttpResponse
from tempfile import NamedTemporaryFile
from PyPDF2 import PdfMerger
# from views_certificado import GeraPDFAluno
from tempfile import NamedTemporaryFile
from django.http import HttpResponse
from PyPDF2 import PdfMerger
from django.shortcuts import get_object_or_404
# from app_cert.views.views_certificado import GeraPDFAluno  # Verifique o caminho correto
from tempfile import NamedTemporaryFile
from django.http import FileResponse


def certificado_novo(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificado_lista')  # Redirecione para a lista após criar
    else:
        form = ModeloForm()

    return render(request, 'certificado/criar.html', {'form': form})

# class GeraPDFTurma(View):
#     def get(self, request, id_turma):
#         # Obtendo todos os alunos da turma fornecida
#         alunos_turma = Aluno.objects.filter(fk_turma=id_turma)

#         # Lista para armazenar as respostas de arquivo para download
#         file_responses = []

#         # Iterando sobre todos os alunos da turma e gerando os certificados
#         for aluno in alunos_turma:
#             # Chamando a view GeraPDFAluno para gerar o PDF de cada aluno
#             response = GeraPDFAluno.as_view()(request, id=aluno.id)

#             # Verificando se a resposta é um HttpResponse válido
#             if isinstance(response, HttpResponse) and response.status_code == 200:
#                 # Criando uma resposta de arquivo para download
#                 file_response = FileResponse(
#                     io.BytesIO(response.content),
#                     content_type='application/pdf'
#                 )
#                 file_response['Content-Disposition'] = f'attachment; filename="{aluno.aluno_nome}_certificado.pdf"'
#                 file_responses.append(file_response)

#         # Combinando todos os certificados em um arquivo ZIP antes de enviar
#         zip_buffer = io.BytesIO()
#         with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED) as zip_file:
#             for i, file_response in enumerate(file_responses, start=1):
#                 zip_file.writestr(f'certificado_{i}.pdf', file_response.getvalue())

#         # Configurando a resposta para o arquivo ZIP
#         response = HttpResponse(
#             zip_buffer.getvalue(),
#             content_type='application/zip'
#         )
#         response['Content-Disposition'] = 'attachment; filename="certificados_turma.zip"'

#         return response

class GeraPDFTurma(View):
    def get(self, request, id_turma):
        # Obtendo a turma
        turma = Turma.objects.get(pk=id_turma)

        # Obtendo todos os alunos da turma fornecida
        alunos_turma = Aluno.objects.filter(fk_turma=id_turma)

        # Lista para armazenar as respostas de arquivo para download
        file_responses = []

        # Iterando sobre todos os alunos da turma e gerando os certificados
        for aluno in alunos_turma:
            # Chamando a view GeraPDFAluno para gerar o PDF de cada aluno
            response = GeraPDFAluno.as_view()(request, id=aluno.id)

            # Verificando se a resposta é um HttpResponse válido
            if isinstance(response, HttpResponse) and response.status_code == 200:
                # Criando uma resposta de arquivo para download
                file_response = FileResponse(
                    io.BytesIO(response.content),
                    content_type='application/pdf'
                )
                file_response['Content-Disposition'] = f'attachment; filename="{aluno.aluno_nome}_{turma.turma}.pdf"'
                file_responses.append(file_response)

        # Combinando todos os certificados em um arquivo ZIP antes de enviar
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED) as zip_file:
            for file_response in file_responses:
                # Obtendo o nome do arquivo do response
                file_name = file_response['Content-Disposition'].split('"')[1]

                # Adicionando o certificado ao arquivo ZIP com o nome do aluno e turma
                zip_file.writestr(file_name, file_response.getvalue())

        # Configurando a resposta para o arquivo ZIP
        response = HttpResponse(
            zip_buffer.getvalue(),
            content_type='application/zip'
        )
        response['Content-Disposition'] = f'attachment; filename="certificados_turma_{turma.turma}.zip"'

        return response





# def certificado_lista(request):
#     # Passo 1: Listar todas as turmas
#     todas_turmas = Turma.objects.all()
#     print(f"Todas as Turmas: {todas_turmas}")

#     # Inicializar um dicionário de contexto para armazenar os alunos com campos em branco por turma
#     context = {}

#     # Passo 2: Pegar os alunos de acordo com sua turma
#     for turma in todas_turmas:
#         alunos_por_turma = Aluno.objects.filter(fk_turma=turma)

#         # Inicializar uma lista para armazenar alunos com campos em branco
#         alunos_com_campos_vazios = []

#         # Passo 3: Verificar se os campos estão vazios
#         for aluno in alunos_por_turma:
#             if not aluno.aluno_cpf or not aluno.aluno_nome or not aluno.aluno_email or not aluno.fk_turma_id:
#                 alunos_com_campos_vazios.append(aluno)

#         # Passo 4: Adicionar os alunos com campos em branco ao contexto, organizado por turma
#         context[turma] = alunos_com_campos_vazios
#         print(f"Print variável CONTEXT: {context}")

#     return render(request, 'certificado/lista.html', {'context': context})


# views_certificado.py

# views_certificado.py

# def certificado_lista(request):
#     # Passo 1: Pegar todos os alunos com os campos vazios especificados
#     alunos_com_campos_vazios = Aluno.objects.filter(
#         Q(aluno_nome='') | Q(aluno_cpf='') | Q(aluno_email='') | Q(fk_turma__isnull=True)
#     )

#     # Inicializar um dicionário de contexto para armazenar os alunos com campos em branco por turma
#     context = {}

#     # Passo 2: Organizar os alunos por turma
#     for aluno in alunos_com_campos_vazios:
#         turma = aluno.fk_turma

#         # Se a turma ainda não estiver no contexto, inicializar uma lista para ela
#         if turma not in context:
#             context[turma] = []

#         # Adicionar o aluno à lista da turma
#         context[turma].append(aluno)

#     print(f"Print variável CONTEXT: {context}")

#     return render(request, 'certificado/lista.html', {'context': context})


# views_certificado.py



# def certificado_lista(request):
#     # Passo 1: Pegar todos os alunos com os campos vazios especificados
#     alunos_com_campos_vazios = Aluno.objects.filter(
#         Q(aluno_nome='') | Q(aluno_cpf='') | Q(aluno_email='') | Q(fk_turma__isnull=True)
#     )

#     # Inicializar um dicionário de contexto para armazenar os alunos com campos em branco por turma
#     context = {}

#     print(f" alunos com campos vazios = {alunos_com_campos_vazios}")

#     # Passo 2: Organizar os alunos por turma
#     for aluno in alunos_com_campos_vazios:
#         turma = aluno.fk_turma

#         # Se a turma não existir no contexto, inicializar uma lista para ela
#         if turma not in context:
#             context[turma] = []

#         # Adicionar o aluno à lista da turma
#         context[turma].append(aluno)

#     print(f"Print variável CONTEXT: {context}")

#     return render(request, 'certificado/lista.html', {'context': context})





def certificado_lista(request):
    # Passo 1: Pegar todos os alunos
    todos_alunos = Aluno.objects.order_by('id')

    # Inicializar um dicionário de contexto para armazenar os alunos com campos em branco por turma
    context = {}

    # Passo 2: Organizar os alunos por turma e verificar campos vazios
    for aluno in todos_alunos:
        turma = aluno.fk_turma

        # Se a turma não existir no contexto, inicializar uma lista vazia para ela
        if turma not in context:
            context[turma] = []

        # Verificar se algum campo está vazio
        campos_vazios = (
            aluno.aluno_nome == '' or
            aluno.aluno_cpf == '' or
            aluno.aluno_email == '' or
            aluno.fk_turma == '' or
            # aluno.aluno_nota == '' or
            # aluno.codigo_hash == '' or
            # aluno.qrcode == '' or
            # aluno.fk_status is None or
            aluno.fk_curso is None or
            aluno.fk_om is None or
            aluno.fk_forca_orgao is None or
            aluno.fk_posto is None or
            aluno.fk_quadro is None or
            aluno.fk_especialidade is None or
            aluno.fk_in_ex is None or
            aluno.fk_tratamento is None
        )

        # Se algum campo estiver vazio, adicionar o aluno à lista da turma
        if campos_vazios:
            context[turma].append(aluno)

    print(f"Print variável CONTEXT: {context}")

    return render(request, 'certificado/lista.html', {'context': context})

def certificado_editar(request, id):
    context = {}
    certificado_ob = get_object_or_404(Modelo, id=id)
    if request.method == 'POST':
        form = ModeloForm(request.POST, instance=certificado_ob)
        if form.is_valid():
            form.save()
            return redirect('certificado_lista')
    else:
        form = ModeloForm(instance=certificado_ob)
    context = {
        'form': form,
        'certificado_ob': certificado_ob
    }
    return render(request, 'certificado/editar.html', context)


def certificado_delete(request, id):
    context = {}
    certificado_ob = get_object_or_404(Modelo, id=id)
    if request.method == 'POST':
        certificado_ob.delete()
        # messages.success(request, 'Registro excluído com sucesso.')
        return redirect('certificado_lista')

    context = {
        'certificado_ob': certificado_ob
    }

    return render(request, 'certificado/excluir.html', context)

class GeraPDFAluno(View):

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        result = finders.find(uri)
        if result:
            if not isinstance(result, (list, tuple)):
                result = [result]
            result = list(os.path.realpath(path) for path in result)
            path = result[0]
        else:
            sUrl = settings.STATIC_URL  # Typically /static/
            sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
            mUrl = settings.MEDIA_URL  # Typically /media/
            mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

            if uri.startswith(mUrl):
                path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                return uri

        # Certifique-se de que o arquivo exista
        if not os.path.isfile(path):
            raise Exception(
                'A URI de mídia deve começar com %s ou %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, id, *args, **kwargs):

        aluno = Aluno.objects.select_related(
            'fk_status',
            'fk_turma',
            'fk_curso',
            'fk_forca_orgao',
            'fk_posto',
            'fk_quadro',
            'fk_especialidade',
            'fk_in_ex',
            'fk_tratamento',
            'fk_turma__fk_assinaturas_ch',
            'fk_turma__fk_assinaturas_dpl',
            
            'fk_turma__fk_img_frente',
            'fk_turma__fk_img_fundo',

            'fk_turma__fk_modelo',
            # 'fk_turma__fk_texto_quem',
            # 'codigo_hash',
            # 'aluno_nota',
        ).get(id=id)

        posto_quadro_esp = f"{aluno.fk_posto} {aluno.fk_quadro} {aluno.fk_especialidade} "

        codigo_hash = aluno.codigo_hash
        qrcode = aluno.qrcode



        # Agora você pode acessar a assinatura relacionada à turma do aluno
        assinatura_turma_ch = aluno.fk_turma.fk_assinaturas_ch
        assinatura_turma_dpl = aluno.fk_turma.fk_assinaturas_dpl

        img_frete = aluno.fk_turma.fk_img_frente.imagem_img

        img_fundo = aluno.fk_turma.fk_img_fundo.imagem_img

        in_ex = str(aluno.fk_in_ex)

        data_curso = []

        if in_ex == 'INTERNO':
            data_certificado = str(aluno.fk_turma.data_turma_interno)

        else:
            data_certificado = str(aluno.fk_turma.data_turma_externo)


        ch = assinatura_turma_ch.imagem
        ch_desc = assinatura_turma_ch.imagem_desc
        ch_img = assinatura_turma_ch.imagem_img

        dpl = assinatura_turma_dpl.imagem
        dpl_desc = assinatura_turma_dpl.imagem_desc
        dpl_img = assinatura_turma_dpl.imagem_img

        texto_modelo = aluno.fk_turma.fk_modelo.fk_texto_modelo
        # print(texto_tipo)
        texto_primeira_parte = aluno.fk_turma.fk_modelo.fk_texto_modelo_desc
        # print(texto_quem)

        texto_motivo = str(aluno.fk_turma.fk_modelo.fk_texto_motivo)
        
        
        status = aluno.fk_status
        # turma = aluno.fk_curso.curso_descricao + 
        ano = aluno.fk_turma.fk_ano_curso
        print(ano)
        turma = aluno.fk_curso.curso_descricao + ' - ' + aluno.fk_turma.turma
        curso = aluno.fk_curso
        tratamento = aluno.fk_tratamento
        # data_curso = ' 06 de asfasf a 25 adfadsfasf 2023'
        # Obtendo a data e hora atuais
        data_e_hora_atuais = datetime.now()

        # Formatando a data e hora atuais como string
        data_e_hora_formatadas = data_e_hora_atuais.strftime('%Y-%m-%d %H:%M:%S')
   
        grade_turmas = GradeTurma.objects.filter(fk_turma=aluno.fk_turma, fk_in_ex=aluno.fk_in_ex).order_by('fk_instrucao__instrucao_sigla')

        tempo_total = 0
        tempos_por_instrucao = []

        for grade_turma in grade_turmas:
            tempo_total += grade_turma.tempo_instrucao
            tempos_por_instrucao.append({
                'tempo': grade_turma.tempo_instrucao,
                'descricao': grade_turma.fk_instrucao.instrucao_descricao
            })

        try:
            template = get_template('certificado/base_cert.html')

            # Contexto original
            base_context = {
                'title': 'PDF Hello',
                'aluno': aluno,
                'posto_quadro_esp': posto_quadro_esp,
                'status': status,
                'turma': turma,
                'curso': curso,
                'tratamento': tratamento,
                'data_curso': data_curso,
                'frente': img_frete,
                'verso': img_fundo,
                'selo': 'img/selo.jpg',
                'om': 'img/om.png',
                'texto_tipo': texto_modelo,
                'texto_primeira_parte': texto_primeira_parte,
                'texto_motivo': texto_motivo,
                'data_certificado': data_certificado,
                'turma': turma,
                'assinatura_ch': ch,
                'assinatura_ch_cargo': ch_desc,
                'assinatura_ch_img': ch_img,
                'assinatura_dpl': dpl,
                'assinatura_dpl_cargo': dpl_desc,
                'assinatura_dpl_img': dpl_img,
                'codigo_hash':codigo_hash,
                'qrcode' : qrcode,
                'data_e_hora_formatadas' : data_e_hora_formatadas
            }

            # Contexto com informações de tempo
            tempo_context = {
                'tempo_total': tempo_total,
                'tempos_por_instrucao': tempos_por_instrucao,
            }

            # Unindo os dois contextos
            context = {**base_context, **tempo_context}
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            pisa_status = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            if pisa_status.err:
                return HttpResponse('Ocorreram erros: <pre>' + html + '</pre>', content_type='text/html')
            return response
        except Exception as e:
            print(str(e))
            return HttpResponseRedirect(reverse_lazy('certificado_lista'))



def certificado_manual(request):
    if request.method == 'POST':
        form = CertExtForm(request.POST)
        if form.is_valid():
            # Process the form data here (save, manipulate, etc.)
            # For example: form.save()
            pass  # Replace 'pass' with your form processing logic
    else:
        form = CertExtForm()
    
    return render(request, 'certificado/manual.html', {'form': form})


## Abaixo ok
# class GeraPDFExterno(View):
#     def link_callback(self, uri, rel):
#         """
#         Convert HTML URIs to absolute system paths so xhtml2pdf can access those
#         resources
#         """
#         result = finders.find(uri)
#         if result:
#             if not isinstance(result, (list, tuple)):
#                 result = [result]
#             result = list(os.path.realpath(path) for path in result)
#             path = result[0]
#         else:
#             sUrl = settings.STATIC_URL  # Typically /static/
#             sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
#             mUrl = settings.MEDIA_URL  # Typically /media/
#             mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

#             if uri.startswith(mUrl):
#                 path = os.path.join(mRoot, uri.replace(mUrl, ""))
#             elif uri.startswith(sUrl):
#                 path = os.path.join(sRoot, uri.replace(sUrl, ""))
#             else:
#                 return uri

#         # Certifique-se de que o arquivo exista
#         if not os.path.isfile(path):
#             raise Exception(
#                 'A URI de mídia deve começar com %s ou %s' % (sUrl, mUrl)
#             )
#         return path

#     def post(self, request):
#         # Obtendo os campos do formulário
#         # tipo = int(request.POST.get('tipo'))
#     #     tipo = request.POST.get('tipo')
#     #     print(tipo)
#     #     primeira_parte = request.POST.get('primeira_parte')
#     #     a_quem = request.POST.get('a_quem')
#     #     motivo = request.POST.get('motivo')
#     #     fk_assinaturas_ch = request.POST.get('fk_assinaturas_ch')
#     #     fk_assinaturas_dpl = request.POST.get('fk_assinaturas_dpl')
#     #     fk_img_frente = request.POST.get('fk_img_frente')

#     #    # Recuperando os dados dos respectivos modelos usando os IDs
#     #     tipo = get_object_or_404(Textos, id=tipo)
#     #     primeira_parte = get_object_or_404(Textos, id=primeira_parte)

#     #     fk_assinaturas_ch = get_object_or_404(Imagem, id=fk_assinaturas_ch)
#     #     # fk_assinaturas_ch_desc = get_object_or_404(Imagem, id=fk_assinaturas_ch)



#         # tipo = request.POST.get('tipo', '')

#         # tipo = get_object_or_404(Textos, id=tipo) if request.POST.get('tipo') != '' else ''
#         # tipo_id = request.POST.get('tipo', '') 
#         # tipo = get_object_or_404(Textos, id=tipo_id) if tipo_id != '' else None

#         # primeira_parte = request.POST.get('primeira_parte', '')
#         # primeira_parte = primeira_parte if primeira_parte else ''  # Expressão ternária

#         # a_quem = request.POST.get('a_quem', '')
#         # a_quem = a_quem if a_quem else ''  # Expressão ternária

#         # motivo = request.POST.get('motivo', '')
#         # motivo = motivo if motivo else ''  # Expressão ternária

#         # fk_assinaturas_ch_id = request.POST.get('fk_assinaturas_ch', '')
#         # fk_assinaturas_ch_id = fk_assinaturas_ch_id if fk_assinaturas_ch_id else ''  # Expressão ternária

#         # fk_assinaturas_dpl_id = request.POST.get('fk_assinaturas_dpl', '')
#         # fk_assinaturas_dpl_id = fk_assinaturas_dpl_id if fk_assinaturas_dpl_id else ''  # Expressão ternária

#         tipo = request.POST.get('tipo', '')

#         if tipo != '':
#             tipo = get_object_or_404(Textos, id=tipo)
#         else:
#             tipo = ''

#         primeira_parte = request.POST.get('primeira_parte', '')
#         if primeira_parte != '':
#             primeira_parte = get_object_or_404(Textos, id=primeira_parte)
#         else:
#             primeira_parte = ''

#         a_quem = request.POST.get('a_quem', '')
#         if a_quem != '':
#             a_quem = a_quem
#         else:
#             a_quem = ''

#         motivo = request.POST.get('motivo', '')
#         if motivo != '':
#             motivo = motivo
#         else:
#             motivo = ''

#         fk_assinaturas_ch_id = request.POST.get('fk_assinaturas_ch', '')
#         print(f'CH : {fk_assinaturas_ch_id}')
#         if fk_assinaturas_ch_id != '':
#             fk_assinaturas_ch_id = get_object_or_404(Imagem, id=fk_assinaturas_ch_id)
#         else:
#             fk_assinaturas_ch_id = ''

#         fk_assinaturas_dpl_id = request.POST.get('fk_assinaturas_dpl', '')
#         if fk_assinaturas_dpl_id != '':
#             fk_assinaturas_dpl_id = get_object_or_404(Imagem, id=fk_assinaturas_dpl_id)
#         else:
#             fk_assinaturas_dpl_id = ''


#         fk_img_frente_id = request.POST.get('fk_img_frente', '')
#         fk_img_frente_id = fk_img_frente_id if fk_img_frente_id else ''  # Expressão ternária


        


#         # if fk_assinaturas_ch_id:  # Verifica se fk_assinaturas_ch não é vazio
#         #     fk_assinaturas_ch = get_object_or_404(Imagem, id=fk_assinaturas_ch_id)
#         #     print(f" cargo {fk_assinaturas_ch.imagem}")
#         #     print(f" cargo desc {fk_assinaturas_ch.imagem_desc}")
#         #     print(f" cargo desc {fk_assinaturas_ch.imagem_img}")

#         # fk_assinaturas_dpl = get_object_or_404(Imagem, id=fk_assinaturas_dpl_id)
#         # print(f" cargo {fk_assinaturas_dpl.imagem}")
#         # print(f" cargo desc {fk_assinaturas_dpl.imagem_desc}")
#         # print(f" cargo desc {fk_assinaturas_dpl.imagem_img}")

#         fk_img_frente = get_object_or_404(Imagem, id=fk_img_frente_id)
#         print(f" image {fk_img_frente.imagem_img}")




#         # Aqui você pode realizar o tratamento e processamento dos campos recebidos do formulário conforme necessário

#         try:
#             template = get_template('certificado/base_externo.html')

#             # Montando o contexto com os dados do formulário
#             base_context = {
#                 'title': a_quem,
#                 'tipo': tipo,
#                 'primeira_parte': primeira_parte,
#                 'a_quem': a_quem,
#                 'motivo': motivo,
#                 'frente': fk_img_frente.imagem_img,

#                 # 'assinatura_dpl': fk_assinaturas_dpl_id.imagem,
#                 # 'assinatura_dpl_cargo': fk_assinaturas_dpl_id.imagem_desc,
#                 # 'assinatura_dpl_img': fk_assinaturas_dpl_id.imagem_img,

#                 # 'assinatura_ch': fk_assinaturas_ch_id.imagem,
#                 # 'assinatura_ch_cargo': fk_assinaturas_ch_id.imagem_desc,
#                 # 'assinatura_ch_img': fk_assinaturas_ch_id.imagem_img,

#                 'assinatura_ch': fk_assinaturas_ch_id.imagem if isinstance(fk_assinaturas_ch_id, Imagem) else '',
#                 'assinatura_ch_cargo': fk_assinaturas_ch_id.imagem_desc if isinstance(fk_assinaturas_ch_id, Imagem) else '',
#                 'assinatura_ch_img': fk_assinaturas_ch_id.imagem_img if isinstance(fk_assinaturas_ch_id, Imagem) else '',


#                 'assinatura_dpl': fk_assinaturas_dpl_id.imagem if isinstance(fk_assinaturas_dpl_id, Imagem) else '',
#                 'assinatura_dpl_cargo': fk_assinaturas_dpl_id.imagem_desc if isinstance(fk_assinaturas_dpl_id, Imagem) else '',
#                 'assinatura_dpl_img': fk_assinaturas_dpl_id.imagem_img if isinstance(fk_assinaturas_dpl_id, Imagem) else '',
#                 # Adicione outros campos do contexto conforme necessário
#             }

#             # Gerando o PDF a partir do template e do contexto
#             html = template.render(base_context)
#             response = HttpResponse(content_type='application/pdf')
#             pisa_status = pisa.CreatePDF(
#                 html, dest=response,
#                 link_callback=self.link_callback
#             )
#             if pisa_status.err:
#                 return HttpResponse('Ocorreram erros: <pre>' + html + '</pre>', content_type='text/html')
#             return response
#         except Exception as e:
#             print(str(e))
#             return HttpResponseRedirect(reverse_lazy('certificado_lista'))




# class GeraPDFExterno(View):
#     def link_callback(self, uri, rel):
#         """
#         Convert HTML URIs to absolute system paths so xhtml2pdf can access those
#         resources
#         """
#         result = finders.find(uri)
#         if result:
#             if not isinstance(result, (list, tuple)):
#                 result = [result]
#             result = list(os.path.realpath(path) for path in result)
#             path = result[0]
#         else:
#             sUrl = settings.STATIC_URL  # Typically /static/
#             sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
#             mUrl = settings.MEDIA_URL  # Typically /media/
#             mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

#             if uri.startswith(mUrl):
#                 path = os.path.join(mRoot, uri.replace(mUrl, ""))
#             elif uri.startswith(sUrl):
#                 path = os.path.join(sRoot, uri.replace(sUrl, ""))
#             else:
#                 return uri

#         # Certifique-se de que o arquivo exista
#         if not os.path.isfile(path):
#             raise Exception(
#                 'A URI de mídia deve começar com %s ou %s' % (sUrl, mUrl)
#             )
#         return path

#     def post(self, request):
#         tipo = request.POST.get('tipo')
#         primeira_parte = request.POST.get('primeira_parte')
#         a_quem = request.POST.get('a_quem')
#         motivo = request.POST.get('motivo')
#         fk_assinaturas_ch = request.POST.get('fk_assinaturas_ch')
#         fk_assinaturas_dpl = request.POST.get('fk_assinaturas_dpl')
#         fk_img_frente = request.POST.get('fk_img_frente')

#         # Verificar se os campos do POST estão vazios e atribuir valores padrão se necessário
#         tipo = get_object_or_404(Textos, id=tipo) if tipo else ""
#         primeira_parte = get_object_or_404(Textos, id=primeira_parte) if primeira_parte else ""
#         fk_assinaturas_ch = get_object_or_404(Imagem, id=fk_assinaturas_ch) if fk_assinaturas_ch else ""
#         fk_assinaturas_dpl = get_object_or_404(Imagem, id=fk_assinaturas_dpl) if fk_assinaturas_dpl else ""
#         fk_img_frente = get_object_or_404(Imagem, id=fk_img_frente) if fk_img_frente else ""

#         try:
#             template = get_template('certificado/base_externo.html')
#             base_context = {
#                 'title': a_quem,
#                 'tipo': tipo,
#                 'primeira_parte': primeira_parte,
#                 'a_quem': a_quem,
#                 'motivo': motivo,
#                 'frente': fk_img_frente.imagem_img,
#                 'assinatura_dpl': fk_assinaturas_dpl.imagem,
#                 'assinatura_dpl_cargo': fk_assinaturas_dpl.imagem_desc,
#                 'assinatura_dpl_img': fk_assinaturas_dpl.imagem_img,
#                 'assinatura_ch': fk_assinaturas_ch.imagem,
#                 'assinatura_ch_cargo': fk_assinaturas_ch.imagem_desc,
#                 'assinatura_ch_img': fk_assinaturas_ch.imagem_img,
#             }

#             html = template.render(base_context)
#             response = HttpResponse(content_type='application/pdf')
#             pisa_status = pisa.CreatePDF(
#                 html, dest=response,
#                 link_callback=self.link_callback
#             )
#             if pisa_status.err:
#                 return HttpResponse('Ocorreram erros: <pre>' + html + '</pre>', content_type='text/html')
#             return response
#         except Exception as e:
#             print(str(e))
#             return HttpResponseRedirect(reverse_lazy('certificado_lista'))

class GeraPDFExterno(View):
    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        result = finders.find(uri)
        if result:
            if not isinstance(result, (list, tuple)):
                result = [result]
            result = list(os.path.realpath(path) for path in result)
            path = result[0]
        else:
            sUrl = settings.STATIC_URL  # Typically /static/
            sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
            mUrl = settings.MEDIA_URL  # Typically /media/
            mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

            if uri.startswith(mUrl):
                path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                return uri

        # Certifique-se de que o arquivo exista
        if not os.path.isfile(path):
            raise Exception(
                'A URI de mídia deve começar com %s ou %s' % (sUrl, mUrl)
            )
        return path

    def post(self, request):
        # Capturando os dados do formulário
        tipo_id = request.POST.get('tipo', '')
        tipo = get_object_or_404(Textos, id=tipo_id) if tipo_id else None

        primeira_parte_id = request.POST.get('primeira_parte', '')
        primeira_parte = get_object_or_404(Textos, id=primeira_parte_id) if primeira_parte_id else None

        a_quem = request.POST.get('a_quem', '')
        motivo = request.POST.get('motivo', '')

        fk_assinaturas_ch_id = request.POST.get('fk_assinaturas_ch', '')
        fk_assinaturas_dpl_id = request.POST.get('fk_assinaturas_dpl', '')

        # Verifica se fk_assinaturas_dpl tem valor e fk_assinaturas_ch não tem valor
        if fk_assinaturas_dpl_id and not fk_assinaturas_ch_id:
            fk_assinaturas_ch_id = fk_assinaturas_dpl_id
            fk_assinaturas_ch = get_object_or_404(Imagem, id=fk_assinaturas_ch_id)
            fk_assinaturas_dpl = None
        else:
            fk_assinaturas_ch = get_object_or_404(Imagem, id=fk_assinaturas_ch_id) if fk_assinaturas_ch_id else None
            fk_assinaturas_dpl = get_object_or_404(Imagem, id=fk_assinaturas_dpl_id) if fk_assinaturas_dpl_id else None



        ##ok aqui
        # fk_assinaturas_ch_id = request.POST.get('fk_assinaturas_ch', '')
        # fk_assinaturas_ch = get_object_or_404(Imagem, id=fk_assinaturas_ch_id) if fk_assinaturas_ch_id else None

        # fk_assinaturas_dpl_id = request.POST.get('fk_assinaturas_dpl', '')
        # fk_assinaturas_dpl = get_object_or_404(Imagem, id=fk_assinaturas_dpl_id) if fk_assinaturas_dpl_id else None
        #--------

        fk_img_frente_id = request.POST.get('fk_img_frente', '')
        fk_img_frente = get_object_or_404(Imagem, id=fk_img_frente_id) if fk_img_frente_id else None

        # Montando o contexto com os dados do formulário
        base_context = {
            'title': a_quem,
            'tipo': tipo,
            'primeira_parte': primeira_parte,
            'a_quem': a_quem,
            'motivo': motivo,
            'frente': fk_img_frente.imagem_img if isinstance(fk_img_frente, Imagem) else '',
            'assinatura_ch': fk_assinaturas_ch.imagem if isinstance(fk_assinaturas_ch, Imagem) else '',
            'assinatura_ch_cargo': fk_assinaturas_ch.imagem_desc if isinstance(fk_assinaturas_ch, Imagem) else '',
            'assinatura_ch_img': fk_assinaturas_ch.imagem_img if isinstance(fk_assinaturas_ch, Imagem) else '',
            'assinatura_dpl': fk_assinaturas_dpl.imagem if isinstance(fk_assinaturas_dpl, Imagem) else '',
            'assinatura_dpl_cargo': fk_assinaturas_dpl.imagem_desc if isinstance(fk_assinaturas_dpl, Imagem) else '',
            'assinatura_dpl_img': fk_assinaturas_dpl.imagem_img if isinstance(fk_assinaturas_dpl, Imagem) else '',
            # Adicione outros campos do contexto conforme necessário
        }

        try:
            # Gerar o PDF a partir do template e do contexto
            template = get_template('certificado/base_externo.html')
            html = template.render(base_context)
            response = HttpResponse(content_type='application/pdf')
            pisa_status = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            if pisa_status.err:
                return HttpResponse('Ocorreram erros: <pre>' + html + '</pre>', content_type='text/html')
            return response
        except Exception as e:
            print(str(e))
            return HttpResponseRedirect(reverse_lazy('certificado_lista'))
