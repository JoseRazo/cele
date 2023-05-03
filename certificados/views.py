from django.shortcuts import render
from django.contrib.auth.decorators import login_required








# Create your views here.

def login_view(request):
    return render(request,"certificados/login.html")

@login_required
def dash_view(request):
    return render(request,"certificados/dashboard.html")





