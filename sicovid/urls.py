"""sicovid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from monitor.views import home, buscar, testar
from paciente import views as pacienteviews

urlpatterns = [
    path('', home),
    path('buscar', buscar),
    path('testar', testar),
    path('admin/', admin.site.urls),

    # paciente
    path('paciente', pacienteviews.paciente),
    path('paciente/show', pacienteviews.show),
    path('paciente/edit/<int:cpf>', pacienteviews.edit),
    path('paciente/update/<int:cpf>', pacienteviews.update),
    path('paciente/delete/<int:cpf>', pacienteviews.destroy),
]
