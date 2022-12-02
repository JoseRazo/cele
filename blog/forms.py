from django import forms

class AspiranteCeleForm(forms.Form):
    nombre = forms.CharField(label='Ingresa tu nombre', min_length=4, max_length=50, required=True)
    email = forms.EmailField(label='Ingresa tu email', max_length=50, required=True)
    asunto = forms.CharField(max_length=255, required=True)
    mensaje = forms.CharField(label='Ingresa tu mensaje', widget=forms.Textarea, min_length=4, required=True)

class AspiranteEdconForm(forms.Form):
    nombre = forms.CharField(label='Ingresa tu nombre', min_length=4, max_length=50, required=True)
    email = forms.EmailField(label='Ingresa tu email', max_length=50, required=True)
    asunto = forms.CharField(max_length=255, required=True)
    mensaje = forms.CharField(label='Ingresa tu mensaje', widget=forms.Textarea, min_length=4, required=True)

class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Ingresa tu nombre', min_length=4, max_length=50, required=True)
    email = forms.EmailField(label='Ingresa tu email', max_length=50, required=True)
    mensaje = forms.CharField(label='Ingresa tu mensaje', widget=forms.Textarea, min_length=4, required=True)
