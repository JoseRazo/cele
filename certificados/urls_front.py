#from .views import 
from django.contrib import admin
from django.urls import path
from .views_front import login_view, dash_view, logout_view, profile_user
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name='certificados'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('dashboard/', dash_view, name="dashboard"),
    path('dashboard/profile/', profile_user, name="profile"),
    path('logout/', logout_view, name="logout"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
