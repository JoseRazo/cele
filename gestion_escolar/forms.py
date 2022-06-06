from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Grupo
import uuid

class GrupoCreationForm(forms.ModelForm):
    def generar_codigo():
        codigo = uuid.uuid4().hex[:6].upper()
        return codigo

    codigo = forms.CharField(initial=generar_codigo, label=_('Número de identificación del grupo'), widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Grupo
        fields = '__all__'
        extra_fields = ['codigo']
