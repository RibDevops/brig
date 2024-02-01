from django.urls import URLPattern, path
import urllib3
from .views import *
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', sgc_home, name='sgc_home'),
    path('sgc_turma_lista', sgc_turma_lista, name="sgc_turma_lista"),
    path('sgc_turma_nova', sgc_turma_nova, name="sgc_turma_nova"),
    path('sgc_turma_editar/<int:id>/', sgc_turma_editar, name="sgc_turma_editar"),
    path('sgc_turma_delete/<int:id>/', sgc_turma_delete, name="sgc_turma_delete"),


    path('sgc_aluno_lista', sgc_aluno_lista, name="sgc_aluno_lista"),
    path('sgc_aluno_novo', sgc_aluno_novo, name="sgc_aluno_novo"),
    path('sgc_aluno_editar/<int:id>/', sgc_aluno_editar, name="sgc_aluno_editar"),
    path('sgc_aluno_delete/<int:id>/', sgc_aluno_delete, name="sgc_aluno_delete"),
    path('sgc_aluno_hash/<int:id>/', sgc_aluno_hash, name="sgc_aluno_hash"),
    path('sgc_aluno_lista_detalhes/<int:id>/', sgc_aluno_lista_detalhes, name='sgc_aluno_lista_detalhes'),

    path('sgc_modelo_lista', sgc_modelo_lista, name="sgc_modelo_lista"),
    path('sgc_modelo_novo', sgc_modelo_novo, name="sgc_modelo_novo"),
    path('sgc_modelo_editar/<int:id>/', sgc_modelo_editar, name="sgc_modelo_editar"),
    path('sgc_modelo_delete/<int:id>/', sgc_modelo_delete, name="sgc_modelo_delete"),

    path('sgc_curso_lista', sgc_curso_lista, name="sgc_curso_lista"),
    path('sgc_curso_novo', sgc_curso_novo, name="sgc_curso_novo"),
    path('sgc_curso_editar/<int:id>/', sgc_curso_editar, name="sgc_curso_editar"),
    path('sgc_curso_delete/<int:id>/', sgc_curso_delete, name="sgc_curso_delete"),
    
    path('sgc_grade_lista', sgc_grade_lista, name="sgc_grade_lista"),
    path('sgc_grade_nova', sgc_grade_nova, name="sgc_grade_nova"),
    path('sgc_grade_editar/<int:id>/', sgc_grade_editar, name="sgc_grade_editar"),
    path('sgc_grade_delete/<int:id>/', sgc_grade_delete, name="sgc_grade_delete"),
    path('sgc_grade_detalhes/<int:turma_id>/', sgc_grade_detalhes, name='grade_detalhes'),

    path('sgc_instrucao_lista', sgc_instrucao_lista, name="sgc_instrucao_lista"),
    path('sgc_instrucao_nova', sgc_instrucao_nova, name="sgc_instrucao_nova"),
    path('sgc_instrucao_editar/<int:id>/', sgc_instrucao_editar, name="sgc_instrucao_editar"),
    path('sgc_instrucao_delete/<int:id>/', sgc_instrucao_delete, name="sgc_instrucao_delete"),

    path('sgc_tipo_lista', sgc_tipo_lista, name="sgc_tipo_lista"),
    path('sgc_tipo_novo', sgc_tipo_novo, name="sgc_tipo_novo"),
    path('sgc_tipo_editar/<int:id>/', sgc_tipo_editar, name="sgc_tipo_editar"),
    path('sgc_tipo_delete/<int:id>/', sgc_tipo_delete, name="sgc_tipo_delete"),

    path('sgc_ano_lista', sgc_ano_lista, name="sgc_ano_lista"),
    path('sgc_ano_novo', sgc_ano_novo, name="sgc_ano_novo"),
    path('sgc_ano_editar/<int:id>/', sgc_ano_editar, name="sgc_ano_editar"),
    path('sgc_ano_delete/<int:id>/', sgc_ano_delete, name="sgc_ano_delete"),

    path('sgc_texto_lista', sgc_texto_lista, name="sgc_texto_lista"),
    path('sgc_texto_novo', sgc_texto_novo, name="sgc_texto_novo"),
    path('sgc_texto_editar/<int:id>/', sgc_texto_editar, name="sgc_texto_editar"),
    path('sgc_texto_delete/<int:id>/', sgc_texto_delete, name="sgc_texto_delete"),

    path('sgc_imagem_lista', sgc_imagem_lista, name="sgc_imagem_lista"),
    path('sgc_imagem_novo', sgc_imagem_nova, name="sgc_imagem_nova"),
    path('sgc_imagem_editar/<int:id>/', sgc_imagem_editar, name="sgc_imagem_editar"),
    path('sgc_imagem_delete/<int:id>/', sgc_imagem_delete, name="sgc_imagem_delete"),

    # path('sgc_assinatura_ch_lista', sgc_assinatura_ch_lista, name="sgc_assinatura_ch_lista"),
    # path('sgc_assinatura_ch_novo', sgc_assinatura_ch_nova, name="sgc_assinatura_ch_nova"),
    # path('sgc_assinatura_ch_editar/<int:id>/', sgc_assinatura_ch_editar, name="sgc_assinatura_ch_editar"),
    # path('sgc_assinatura_ch_delete/<int:id>/', sgc_assinatura_ch_delete, name="sgc_assinatura_ch_delete"),

    path('sgc_tratamento_lista', sgc_tratamento_lista, name="sgc_tratamento_lista"),
    path('sgc_tratamento_novo', sgc_tratamento_novo, name="sgc_tratamento_novo"),
    path('sgc_tratamento_editar/<int:id>/', sgc_tratamento_editar, name="sgc_tratamento_editar"),
    path('sgc_tratamento_delete/<int:id>/', sgc_tratamento_delete, name="sgc_tratamento_delete"),

    # path('sgc_funpdf/', sgc_ListaAlunosPDFPdfVie.as_view(), name="sgc_funpdf"),
    # path('sgc_funpdf/', sgc_ListaAlunosPDFPdfView.as_view(), name="sgc_funpdf"),
    # path('sgc_editar/<int:id>/', sgc_GeraPDFAluno.as_view(), name="sgc_geraPDFAluno"),
    path('sgc_geraPDFAluno/<int:id>/', GeraPDFAluno.as_view(), name="sgc_geraPDFAluno"),

    path('sgc_certificado_lista/', sgc_certificado_lista, name="sgc_certificado_lista"),
    path('sgc_certificado_turma_lista/<int:id>/', sgc_certificado_turma_lista, name="sgc_certificado_turma_lista"),
    path('sgc_certificado_manual/', sgc_certificado_manual, name="sgc_certificado_manual"),
    path('sgc_gerar_certificados_turma/<int:id_turma>/', GeraPDFTurma.as_view(), name="sgc_gerar_certificados_turma"),
    path('sgc_certificado_ext/', sgc_certificado_ext, name="sgc_certificado_ext"),
    path('sgc_gerar_certificados_externo/', GeraPDFExterno.as_view(), name="sgc_gerar_certificados_externo"),


    # path('sgc_load-om/', sgc_load_om, name='ajax_load_om'), # AJAX
    # path('sgc_load-om/', sgc_load_om, name='ajax_load_om'),  # Verifique se o nome da função está correto
    path('sgc_ajax_load_related_data_om/', sgc_ajax_load_related_data_om, name="sgc_ajax_load_related_data_om"),
    path('sgc_import_csv_view/', sgc_import_csv_view, name="sgc_import_csv_view"),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


