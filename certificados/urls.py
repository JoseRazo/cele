#from .views import 
from django.contrib import admin
from django.urls import path
from .views import login_view, dash_view, logout_view, profile_user, pdfgen, listar_cursos, mostrar_curso
from django.conf.urls import url





app_name='certificados'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('dashboard/', dash_view, name="dashboard"),
    path('dashboard/profile/', profile_user, name="profile"),
    path('logout/', logout_view, name="logout"),
    path('pdfgen/<curso_id>/<firma>', pdfgen, name="pdfgen"),
    path('mis_cursos/', listar_cursos, name="mis_cursos"),
    path('mis_cursos_detail/<curso_id>', mostrar_curso, name="mis_cursos_detail"),
]

