#from .views import 
from django.contrib import admin
from django.urls import path
from .views_back import pdfgen, pdfget, listar_cursos, mostrar_curso, CursosAlumnoCeleListView, SearchCursosAlumnoCeleView, CursosEstudianteEdconListView, SearchCursosEstudianteEdconView
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name='certificados_back'

urlpatterns = [
    path('pdfgen/<curso_id>/<firma>/<type>', pdfgen, name="pdfgen"),
    path('pdfget/<certfolio>', pdfget, name="pdfget"),
    path('mis_cursos/', listar_cursos, name="mis_cursos"),
    path('mis_cursos_detail/<curso_id>', mostrar_curso, name="mis_cursos_detail"),
    path('certi-cele/', CursosAlumnoCeleListView.as_view(template_name="certificados/certi_cele.html"), name="certi_cele"),
    path('certi-cele-search/', SearchCursosAlumnoCeleView.as_view(template_name="certificados/certi_cele.html"), name='certi_cele_search'),
    path('certi-edcon/', CursosEstudianteEdconListView.as_view(template_name="certificados/certi_edcon.html"), name="certi_edcon"),
    path('certi-edcon-search/', SearchCursosEstudianteEdconView.as_view(template_name="certificados/certi_edcon.html"), name='certi_edcon_search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 