from django.contrib import admin
from django.urls import path

from . import views
from .views import CursoEdconListView, SearchEdconView, CursoCeleListView, SearchCeleView, ValidarCertificadoListView, SearchCertificadoView
from django.conf.urls import url

app_name='blog'

urlpatterns = [
    path('', views.home, name="home"),
    path('cursos-cele/', CursoCeleListView.as_view(), name="cursos_cele"),
    path('cursos-cele/<slug:slug>/', views.cursoCeleDetalle, name="curso_cele_detalle"),
    path('form-aspirante-cele', views.formAspiranteCele, name="form_aspirante_cele"),
    path('cursos-cele-search/', SearchCeleView.as_view(), name='cursos_cele_search'),
    path('cursos-edcon/', CursoEdconListView.as_view(), name="cursos_edcon"),
    path('cursos-edcon/<slug:slug>/', views.cursoEdconDetalle, name="curso_edcon_detalle"),
    path('form-aspirante-edcon', views.formAspiranteEdcon, name="form_aspirante_edcon"),
    path('cursos-edcon-search/', SearchEdconView.as_view(), name='cursos_edcon_search'),
    path('validar-certificado/', ValidarCertificadoListView.as_view(), name="validar_certificado"),
    path('validar-certificado-search/', SearchCertificadoView.as_view(), name='validar_certificado_search'),

    path('contacto/', views.contacto, name="contacto"),
    path('form-contacto', views.formContacto, name="form_contacto"),
]