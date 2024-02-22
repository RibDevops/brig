import statistics
from django.contrib import admin
from django.urls import path, include

from core import settings
from .views import *
from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('sgu', home, name='sgu'),
#     # path('perfil/', home, name='perfil'),

#     # path('create_number/<tipo_id>', create_number, name="create_number"),
#     # path('cadastrar_number/', cadastrar_number, name="cadastrar_number"),

#     # path('create_tipo/', create_tipo, name="create_tipo"),
#     # path('create_setor/', create_setor, name="create_setor"),
#     # # path('create_destino/', create_destino, name="create_destino"),
    
    
#     # path('list_tipo/', list_tipo, name="list_tipo"),

#     # path('list_view/<int:id>/', list_view, name='list_view'),
#     # path('delete_number/<int:id>/', delete_number, name='delete_number'),
#     # path('edit_number/<int:id>/', edit_number, name='edit_number'),
#     path('login/', auth_views.LoginView.as_view(
#         template_name = 'usuarios/form.html'
#     ), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     # path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),



# ]

urlpatterns = [
   
    path('scp_espe_lista/', scp_espe_lista, name="scp_espe_lista"),
    path('scp_espe_nova/', scp_espe_nova, name="scp_espe_nova"),
    path('scp_espe_detalhes/<int:id>/', scp_espe_detalhes, name="scp_espe_detalhes"),
    path('scp_espe_editar/<int:id>/', scp_espe_editar, name="scp_espe_editar"),
    path('scp_espe_delete/<int:id>/', scp_espe_delete, name="scp_espe_delete"),

    path('scp_forca_lista/', scp_forca_lista, name="scp_forca_lista"),
    path('scp_forca_nova/', scp_forca_nova, name="scp_forca_nova"),
    path('scp_forca_delete/<int:id>/', scp_forca_delete, name="scp_forca_delete"),
    path('scp_forca_editar/<int:id>/', scp_forca_editar, name="scp_forca_editar"),

    path('scp_om_lista/', scp_om_lista, name="scp_om_lista"),
    path('scp_om_nova/', scp_om_nova, name="scp_om_nova"),
    path('scp_om_detalhes/<int:id>/', scp_om_detalhes, name="scp_om_detalhes"),
    path('scp_om_editar/<int:id>/', scp_om_editar, name="scp_om_editar"),
    path('scp_om_delete/<int:id>/', scp_om_delete, name="scp_om_delete"),

    path('scp_posto_lista/', scp_posto_lista, name="scp_posto_lista"),
    path('scp_posto_novo/', scp_posto_novo, name="scp_posto_novo"),
    path('scp_posto_detalhes/<int:id>/', scp_posto_detalhes, name="scp_posto_detalhes"),
    path('scp_posto_editar/<int:id>/', scp_posto_editar, name="scp_posto_editar"),
    path('scp_posto_delete/<int:id>/', scp_posto_delete, name="scp_posto_delete"),

    path('scp_quadro_lista/', scp_quadro_lista, name="scp_quadro_lista"),
    path('scp_quadro_novo/', scp_quadro_novo, name="scp_quadro_novo"),
    path('scp_quadro_detalhes/<int:id>/', scp_quadro_detalhes, name="scp_quadro_detalhes"),
    path('scp_quadro_editar/<int:id>/', scp_quadro_editar, name="scp_quadro_editar"),
    path('scp_quadro_delete/<int:id>/', scp_quadro_delete, name="scp_quadro_delete"),

]
