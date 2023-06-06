"""
URL configuration for proyecto_Bisaguirre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('formulario_empleado/', views.formulario_empleado, name='formulario_empleado'),
    path('formulario_proyecto/', views.formulario_proyecto, name='formulario_proyecto'),
    path('formulario_tarea/', views.formulario_tarea, name='formulario_tarea'),
]
