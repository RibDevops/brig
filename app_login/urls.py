from django import views
from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout', views.custom_logout, name='logout'),
    # path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),    
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    # path('plataforma/', views.plataforma, name='plataforma'),
    path('reset/', views.reset, name='reset'),
    
]