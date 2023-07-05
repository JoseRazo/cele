from django import forms
from gestion_escolar.models import Alumno


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['avatar']



