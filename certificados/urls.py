#from .views import 
from django.contrib import admin
from django.urls import path
from .views import login_view, dash_view, logout_view
from django.conf.urls import url


app_name='certificados'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('dashboard/', dash_view, name="dashboard"),
    
]
