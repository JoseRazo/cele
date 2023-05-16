#from .views import 
from django.contrib import admin
from django.urls import path
from .views_back import pdfgen, listar_cursos, mostrar_curso
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name='certificados_back'

urlpatterns = [
    path('pdfgen/<curso_id>/<firma>', pdfgen, name="pdfgen"),
    path('mis_cursos/', listar_cursos, name="mis_cursos"),
    path('mis_cursos_detail/<curso_id>', mostrar_curso, name="mis_cursos_detail"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
