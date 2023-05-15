from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Curso

# Create your views here.

# def home(request):
#     response = redirect('/admin/')
#     return response

class AlumnosCursoList(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        curso=request.data['curso']
        alumnos_grupos={}
        if curso:
            alumnos_grupos=Curso.objects.get(id=curso).alumnos_grupos.all()
            alumno_grupo={p.nombre:p.id for p in alumnos_grupos}
        else:
            alumno_grupo={}
        return JsonResponse(data=alumno_grupo, safe=False)
