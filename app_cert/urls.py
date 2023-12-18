from django.urls import URLPattern, path
import urllib3
from app_cert.views.views_turma import *
from app_cert.views.views_textos import *
from app_cert.views.views_curso import *
from app_cert.views.views_aluno import *
from app_cert.views.views_certificado import *
from app_cert.views.views_modelo import *
from app_cert.views.views_tipo import *
from app_cert.views.views_ano import *
from app_cert.views.views_grade import *
from app_cert.views.views_imagem import *
from app_cert.views.views_import import *
# from app_cert.views.views_assinatura_dpl import *
from app_cert.views.views_tratamento import *
from app_cert.views.views_instrucao import *
from app_cert.views.views_pdf import *
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static

# from .views import Index2View, IndexView

# if settings.DEBUG:
#     URLPattern += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    # path('cert', include('core.urls')),
    path('', home, name='home'),
    path('turma_lista', turma_lista, name="turma_lista"),
    path('turma_nova', turma_nova, name="turma_nova"),
    path('turma_editar/<int:id>/', turma_editar, name="turma_editar"),
    path('turma_delete/<int:id>/', turma_delete, name="turma_delete"),


    path('aluno_lista', aluno_lista, name="aluno_lista"),
    path('aluno_novo', aluno_novo, name="aluno_novo"),
    path('aluno_editar/<int:id>/', aluno_editar, name="aluno_editar"),
    path('aluno_delete/<int:id>/', aluno_delete, name="aluno_delete"),
    path('aluno_hash/<int:id>/', aluno_hash, name="aluno_hash"),

    path('modelo_lista', modelo_lista, name="modelo_lista"),
    path('modelo_novo', modelo_novo, name="modelo_novo"),
    path('modelo_editar/<int:id>/', modelo_editar, name="modelo_editar"),
    path('modelo_delete/<int:id>/', modelo_delete, name="modelo_delete"),

    path('curso_lista', curso_lista, name="curso_lista"),
    path('curso_novo', curso_novo, name="curso_novo"),
    path('curso_editar/<int:id>/', curso_editar, name="curso_editar"),
    path('curso_delete/<int:id>/', curso_delete, name="curso_delete"),
    
    path('grade_lista', grade_lista, name="grade_lista"),
    path('grade_nova', grade_nova, name="grade_nova"),
    path('grade_editar/<int:id>/', grade_editar, name="grade_editar"),
    path('grade_delete/<int:id>/', grade_delete, name="grade_delete"),
    path('grade_detalhes/<int:turma_id>/', grade_detalhes, name='grade_detalhes'),

    path('instrucao_lista', instrucao_lista, name="instrucao_lista"),
    path('instrucao_nova', instrucao_nova, name="instrucao_nova"),
    path('instrucao_editar/<int:id>/', instrucao_editar, name="instrucao_editar"),
    path('instrucao_delete/<int:id>/', instrucao_delete, name="instrucao_delete"),

    path('tipo_lista', tipo_lista, name="tipo_lista"),
    path('tipo_novo', tipo_novo, name="tipo_novo"),
    path('tipo_editar/<int:id>/', tipo_editar, name="tipo_editar"),
    path('tipo_delete/<int:id>/', tipo_delete, name="tipo_delete"),

    path('ano_lista', ano_lista, name="ano_lista"),
    path('ano_novo', ano_novo, name="ano_novo"),
    path('ano_editar/<int:id>/', ano_editar, name="ano_editar"),
    path('ano_delete/<int:id>/', ano_delete, name="ano_delete"),

    path('texto_lista', texto_lista, name="texto_lista"),
    path('texto_novo', texto_novo, name="texto_novo"),
    path('texto_editar/<int:id>/', texto_editar, name="texto_editar"),
    path('texto_delete/<int:id>/', texto_delete, name="texto_delete"),

    path('imagem_lista', imagem_lista, name="imagem_lista"),
    path('imagem_novo', imagem_nova, name="imagem_nova"),
    path('imagem_editar/<int:id>/', imagem_editar, name="imagem_editar"),
    path('imagem_delete/<int:id>/', imagem_delete, name="imagem_delete"),

    # path('assinatura_ch_lista', assinatura_ch_lista, name="assinatura_ch_lista"),
    # path('assinatura_ch_novo', assinatura_ch_nova, name="assinatura_ch_nova"),
    # path('assinatura_ch_editar/<int:id>/', assinatura_ch_editar, name="assinatura_ch_editar"),
    # path('assinatura_ch_delete/<int:id>/', assinatura_ch_delete, name="assinatura_ch_delete"),

    path('tratamento_lista', tratamento_lista, name="tratamento_lista"),
    path('tratamento_novo', tratamento_novo, name="tratamento_novo"),
    path('tratamento_editar/<int:id>/', tratamento_editar, name="tratamento_editar"),
    path('tratamento_delete/<int:id>/', tratamento_delete, name="tratamento_delete"),

    # path('funpdf/', ListaAlunosPDFPdfVie.as_view(), name="funpdf"),
    # path('funpdf/', ListaAlunosPDFPdfView.as_view(), name="funpdf"),
    # path('editar/<int:id>/', GeraPDFAluno.as_view(), name="geraPDFAluno"),
    path('geraPDFAluno/<int:id>/', GeraPDFAluno.as_view(), name="geraPDFAluno"),

    path('certificado_lista/', certificado_lista, name="certificado_lista"),
    path('certificado_manual/', certificado_manual, name="certificado_manual"),
    # path('GeraPDFTurma/<int:id>/', GeraPDFTurma, name="GeraPDFTurma"),
    path('gerar_certificados_turma/<int:id_turma>/', GeraPDFTurma.as_view(), name='gerar_certificados_turma'),
    path('gerar_certificados_externo/', GeraPDFExterno.as_view(), name='gerar_certificados_externo'),
    # path('testaPDFAluno/', pdf_report_create, name="testaPDFAluno"),
    # urllib3(r'^download$', render_pdf),

    # path('load-om/', load_om, name='ajax_load_om'), # AJAX
    # path('load-om/', load_om, name='ajax_load_om'),  # Verifique se o nome da função está correto
    path('ajax_load_related_data_om/', ajax_load_related_data_om, name='ajax_load_related_data_om'),
    path('import_csv_view/', import_csv_view, name='import_csv_view'),


    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ] 

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
