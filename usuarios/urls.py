from django.urls import path
from .views import *

urlpatterns = [
    path('ciudades/', CiudadList.as_view()),
]