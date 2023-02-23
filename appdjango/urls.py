"""appdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from autos import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.registro, name="registro"),
    path('autos/', views.autos, name="autos"),
    path('autos/<int:auto_id>', views.auto_editar, name="editar_auto"),
    path('inicio/', views.inicio, name="inicio"),
    path("cerrarsesion/", views.cerrar_sesion, name="cerrarsesion"),
    path("iniciarsesion/", views.iniciar_sesion, name="iniciarsesion"),
    path("nuevoAuto/",views.crear_auto, name="nuevoAuto"),
    path("nuevoAuto/<int:auto_id>",views.auto_detalle, name="auto_detalle"),
    
]


urlpatterns += staticfiles_urlpatterns()