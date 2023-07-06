#from .views import 
from django.contrib import admin
from django.urls import path
from .views import (
    realizar_encuesta, 
    EncuestaAlumnoCeleListView, 
    SearchEncuestaAlumnoCeleView,
    EncuestaEstudianteEdconListView,
    SearchEncuestaEstudianteEdconView,
    RegistroCeleListView,
    SearchRegistroCeleView,
    RegistroEdconListView,
    SearchRegistroEdconView
    )
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name='encuestas'

urlpatterns = [
    path('encuestas-cele/', EncuestaAlumnoCeleListView.as_view(template_name="encuestas/encuestas_cele.html"), name='encuestas_cele'),
    path('encuestas-cele-search/', SearchEncuestaAlumnoCeleView.as_view(template_name="encuestas/encuestas_cele.html"), name='encuestas_cele_search'),
    path('encuestas-edcon/', EncuestaEstudianteEdconListView.as_view(template_name="encuestas/encuestas_edcon.html"), name='encuestas_edcon'),
    path('encuestas-edcon-search/', SearchEncuestaEstudianteEdconView.as_view(template_name="encuestas/encuestas_edcon.html"), name='encuestas_edcon_search'),
    path('reportes-cele/', RegistroCeleListView.as_view(template_name="encuestas/reportes_cele.html"), name='reportes_cele'),
    path('reportes-cele-search/', SearchRegistroCeleView.as_view(template_name="encuestas/reportes_cele.html"), name='reportes_cele_search'),
    path('reportes-edcon/', RegistroEdconListView.as_view(template_name="encuestas/reportes_edcon.html"), name='reportes_edcon'),
    path('reportes-edcon-search/', SearchRegistroEdconView.as_view(template_name="encuestas/reportes_edcon.html"), name='reportes_edcon_search'),
    path('realizar_encuesta/<curso_id>/<type>', realizar_encuesta, name="realizar_encuesta"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 