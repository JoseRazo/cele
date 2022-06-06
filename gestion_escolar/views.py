from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    response = redirect('/admin/')
    return response