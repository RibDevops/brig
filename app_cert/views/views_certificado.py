import time
import zipfile
import io
import os
from django import template
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from ..utils import *
from ..models import *
from ..forms import *
from django.db.models import Count
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.template.loader import render_to_string, get_template
from django.views.generic import View
from reportlab.pdfgen import canvas
from xhtml2pdf import pisa
from django.conf import settings
from django.contrib.staticfiles import finders
from datetime import datetime
from PyPDF2 import PdfMerger
from django.db.models import Q
from collections import defaultdict
from .views_aluno import sgc_aluno_hash
from django.db.models import Q
import time



def sgc_certificado_novo(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sgc_certificado_lista')  # Redirecione para a lista após criar
    else:
        form = ModeloForm()

    return render(request, 'certificado/criar.html', {'form': form})

class GeraPDFTurma(View):
    def get(self, request, id_turma):
        # Obtendo a turma
        turma = Turma.objects.get(pk=id_turma)

        # Obtendo todos os alunos da turma fornecida
        alunos_turma = Aluno.objects.filter(fk_turma=id_turma)
        # print(alunos_turma)

        # Lista para armazenar as respostas de arquivo para download
        file_responses = []

        # for aluno_hash in alunos_turma:

        #     sgc_aluno_hash(aluno_hash.id)

        for aluno_hash in alunos_turma:
            
            aluno_id_hash = int(aluno_hash.id)
            print(f"id - {aluno_id_hash}")
            sgc_aluno_hash(request, aluno_id_hash)
        
        

        print("Início do programa")
        time.sleep(3)
        print("Fim do programa")

        # Iterando sobre todos os alunos da turma e gerando os certificados
        for aluno in alunos_turma:

        # Adicionando uma pausa de 2 segundos
            
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


def sgc_certificado_lista(request):
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
            # aluno.fk_curso is None or
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

    # print(f"Print variável CONTEXT: {context}")

    return render(request, 'certificado/lista.html', {'context': context})

def sgc_certificado_editar(request, id):
    context = {}
    certificado_ob = get_object_or_404(Modelo, id=id)
    if request.method == 'POST':
        form = ModeloForm(request.POST, instance=certificado_ob)
        if form.is_valid():
            form.save()
            return redirect('sgc_certificado_lista')
    else:
        form = ModeloForm(instance=certificado_ob)
    context = {
        'form': form,
        'certificado_ob': certificado_ob
    }
    return render(request, 'certificado/editar.html', context)


def sgc_certificado_delete(request, id):
    context = {}
    certificado_ob = get_object_or_404(Modelo, id=id)
    if request.method == 'POST':
        certificado_ob.delete()
        # messages.success(request, 'Registro excluído com sucesso.')
        return redirect('sgc_certificado_lista')

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
            # 'fk_curso',
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
        print(f'in_ex: {in_ex}')

        data_curso = []

        if in_ex == '1':
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

        curso_descricao = aluno.fk_turma.turma
        # turma = curso_descricao + ' - ' + aluno.fk_turma.turma
        turma = curso_descricao
        
        status = aluno.fk_status
        ano = aluno.fk_turma.fk_ano_curso
        print(ano)
        # turma = aluno.fk_curso.curso_descricao + ' - ' + aluno.fk_turma.turma
        curso = aluno.fk_turma.turma
        tratamento = aluno.fk_tratamento
        # data_curso = ' 06 de asfasf a 25 adfadsfasf 2023'
        # Obtendo a data e hora atuais
        data_e_hora_atuais = datetime.now()

        # Formatando a data e hora atuais como string
        data_e_hora_formatadas = data_e_hora_atuais.strftime('%Y-%m-%d %H:%M:%S')
   
        # grade_turmas = GradeTurma.objects.filter(fk_turma=aluno.fk_turma, fk_in_ex=aluno.fk_in_ex).order_by('fk_instrucao__instrucao_sigla')

        
        # User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True))
        # grade_turmas = GradeTurma.objects.filter(fk_turma=aluno.fk_turma).filter(Q(interno=in_ex) | Q(externo=in_ex))
        # from django.db.models import Q



        if in_ex == '1':
            grade_turmas = GradeTurma.objects.filter(fk_turma=aluno.fk_turma, interno=in_ex)
        else:
            grade_turmas = GradeTurma.objects.filter(fk_turma=aluno.fk_turma, externo=in_ex)

        # Filtrando as instruções para o aluno atual baseado no tipo (interno ou externo)
        instrucoes_aluno = grade_turmas.values_list('fk_instrucao_id', flat=True).distinct()

        # Recuperando todas as instruções do aluno baseado nos IDs filtrados
        instrucoes = Instrucao.objects.filter(id__in=instrucoes_aluno)

        # Visualizando as instruções do aluno
        for instrucao in instrucoes:
            print(f"Instrução do aluno: {instrucao}")


        tempo_total = 0
        tempos_por_instrucao = []

        for grade_turma in grade_turmas:
            if grade_turma.tempo_instrucao is not None:
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
                'aluno': aluno.aluno_nome,
                'posto_quadro_esp': posto_quadro_esp,
                'status': status,
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



def sgc_certificado_manual(request):
    if request.method == 'POST':
        form = CertExtForm(request.POST)
        if form.is_valid():
            # Process the form data here (save, manipulate, etc.)
            # For example: form.save()
            pass  # Replace 'pass' with your form processing logic
    else:
        form = CertExtForm()
    
    return render(request, 'certificado/manual.html', {'form': form})


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
