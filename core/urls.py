"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sgc/', include('app_cert.urls')),#sistema de gerenciamento de certificados
    path('sgu/', include('app_postos.urls')),#sitenma de gerenciamento de força, posto, quadro
    path('scn/', include('app_scn.urls')),#sistema de numeração de doc da dci
    path('ssa/', include('app_arq.urls')),#sistema de numeração de doc da dci
]
