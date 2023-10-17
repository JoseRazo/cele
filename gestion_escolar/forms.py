from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import Group
from django.contrib.admin.widgets import FilteredSelectMultiple
from utils.meses import MONTHS_SPANISH
from usuarios.models import Usuario
from .models import Alumno, Profesor, Periodo

class AlumnoCreationForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(label='Roles', queryset=Group.objects.filter(name='Alumnos CELE'), required=False, widget=FilteredSelectMultiple('Roles', False))

    def generate_matricula():
        cve_uni = 61
        año = timezone.now().strftime('%y')
        last_user = Alumno.objects.last()
        if not last_user:
            return str(año) + str(cve_uni) + '2' + '0001'
        else:
            matricula = last_user.username
            consecutivo = int(matricula[-4:]) + 1
            matricula = str(año) + str(cve_uni) + '2' + str(consecutivo).zfill(4)
            return matricula

    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', initial=generate_matricula, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    password2 = forms.CharField(label='Confirmar Contraseña', initial=generate_matricula, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    username = forms.CharField(max_length=9, initial=generate_matricula, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    contraseña = forms.CharField(label='Contraseña para pagos', initial=generate_matricula, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Alumno
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(AlumnoCreationForm, self).__init__(*args, **kwargs)
        self.fields['contraseña'].widget = forms.HiddenInput()

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(AlumnoCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AlumnoChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    groups = forms.ModelMultipleChoiceField(label='Roles', queryset=Group.objects.filter(name='Alumnos CELE'), required=False, widget=FilteredSelectMultiple('Roles', False))
    
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    password = ReadOnlyPasswordHashField()
    contraseña = forms.CharField(label='Contraseña para pagos', widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Alumno
        fields = ('username', 'password')
    
    def __init__(self, *args, **kwargs):
        super(AlumnoChangeForm, self).__init__(*args, **kwargs)
        self.fields['contraseña'].widget = forms.HiddenInput()

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class ProfesorCreationForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(label='Roles', queryset=Group.objects.filter(name='Profesores CELE'), required=False, widget=FilteredSelectMultiple('Roles', False))
    
    def generate_password():
        password = Usuario.objects.make_random_password()
        return password
        


    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', initial=generate_password,)
    password2 = forms.CharField(label='Confirmar Contraseña',)

    class Meta:
        model = Profesor
        fields = ('username', 'password')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(ProfesorCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# class ProfesorChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
    
#     username = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
#     password = forms.CharField(label='Cambiar Contraseña',)
#     # password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = Profesor
#         fields = ('username', 'password')

#     def clean_password(self):
#         # Check that the two password entries match
#         password = self.cleaned_data.get("password")
#         return password

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(ProfesorChangeForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user

class CalificacionCursoForm(forms.ModelForm):
    calificacion_final = forms.CharField(initial=0, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class CalificacionCursoSemanalForm(forms.ModelForm):
    calificacion_final = forms.CharField(initial=0, widget=forms.TextInput)

# class GrupoCreationForm(forms.ModelForm):
#     def generar_codigo():
#         codigo = uuid.uuid4().hex[:6].upper()
#         return codigo

#     codigo = forms.CharField(initial=generar_codigo, label=_('Número de identificación del grupo'),
#                              widget=forms.TextInput(attrs={'readonly': 'readonly'}))

#     class Meta:
#         model = Grupo
#         fields = '__all__'
#         extra_fields = ['codigo']

class PeriodoCreationForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'vTextField', 
                'readonly': 'readonly', 
                'placeholder': 'El nombre se autogenera con las fechas seleccionadas.'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        
        inicio_mes = MONTHS_SPANISH.get(self.cleaned_data.get('fecha_inicio').strftime('%B'))
        fin_mes = MONTHS_SPANISH.get(self.cleaned_data.get('fecha_fin').strftime('%B'))
        nombre = f'{self.cleaned_data.get("fecha_inicio").day} {inicio_mes} al {self.cleaned_data.get("fecha_fin").day} {fin_mes} del {self.cleaned_data.get("fecha_fin").year}'
        
        if Periodo.objects.filter(nombre=nombre).exclude(pk=self.instance.pk).exists():
            raise ValidationError({'nombre': ['Ya existe un/a Periodo con este/a Nombre.']})

        cleaned_data['nombre'] = nombre  # Asignar el nombre generado
        return cleaned_data
