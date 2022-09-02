from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from sistema.models import Pais, Estado, Ciudad, Colonia

class CiudadList(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        estado=request.data['estado']
        ciudades={}
        if estado:
            ciudades=Estado.objects.get(id=estado).ciudades.all()
            ciudad={p.nombre:p.id for p in ciudades}
        else:
            ciudad={}
        return JsonResponse(data=ciudad, safe=False)