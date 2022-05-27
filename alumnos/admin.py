from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import Alumno

class AlumnoCreationForm(forms.ModelForm):
    # def generate_matricula():
    #     alumno =  Alumno.objects.last()
    #     matricula = alumno.matricula
    #     if not matricula:
    #         return '612200001'
    #     matricula = matricula.username
    #     return matricula

    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    # matricula = forms.CharField(max_length=9, initial=generate_matricula)

    class Meta:
        model = Alumno
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
    
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Alumno
        fields = ('username', 'password')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


@admin.register(Alumno)
class AlumnoAdmin(DjangoUserAdmin):
    form = AlumnoChangeForm
    add_form = AlumnoCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Datos Generales'), {'fields': ('tipo_usuario', 'nombre', 'apellido_paterno',
         'apellido_materno', 'email', 'telefono', 'avatar')}),
        (_('Domicilio Actual'), {'fields': (
            'estado', 'ciudad', 'colonia', 'calle', 'num_exterior', 'num_interior')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = (
        'username', 'email', 'nombre', 'tipo_usuario'
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        (_('Datos Generales'), {'fields': ('tipo_usuario', 'nombre', 'apellido_paterno',
         'apellido_materno', 'email', 'telefono', 'avatar')}),
        (_('Domicilio Actual'), {'fields': (
            'estado', 'ciudad', 'colonia', 'calle', 'num_exterior', 'num_interior')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

