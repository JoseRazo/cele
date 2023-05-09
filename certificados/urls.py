#from .views import 
from django.contrib import admin
from django.urls import path
from .views import login_view, dash_view, logout_view, profile_user, pdfgenerator, mostrar_cursos
from django.conf.urls import url





app_name='certificados'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('dashboard/', dash_view, name="dashboard"),
    path('dashboard/profile/', profile_user, name="profile"),
    path('logout/', logout_view, name="logout"),
    path('pdfgenerator', pdfgenerator, name="pdfgenerator"),
    path('mis_cursos/', mostrar_cursos, name="mis_cursos"),
]

