from django import forms
from usuarios.models import Usuario


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario  # Change this to use the Usuario model
        fields = ['avatar']

    avatar = forms.ImageField(required=False)



