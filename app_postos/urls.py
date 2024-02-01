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
    path('sgu', home, name='sgu'),
    path('scp_om_lista/', scp_om_lista, name="scp_om_lista"),
    path('scp_om_nova/', scp_om_nova, name="scp_om_nova"),
    path('scp_om_detalhes/<int:id>/', scp_om_detalhes, name="scp_om_detalhes"),
    path('scp_om_ditar/<int:id>/', scp_om_ditar, name="scp_om_ditar"),

    path('scp_espe_lista/', scp_espe_lista, name="scp_espe_lista"),
    path('scp_espe_nova/', scp_espe_nova, name="scp_espe_nova"),
    path('scp_espe_detalhes/<int:id>/', scp_espe_detalhes, name="scp_espe_detalhes"),
    path('scp_espe_ditar/<int:id>/', scp_espe_ditar, name="scp_espe_ditar"),
]
