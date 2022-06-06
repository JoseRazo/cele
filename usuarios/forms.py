from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm, UsernameField
from django.contrib.admin.forms import AdminAuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .models import Usuario, Alumno, Profesor

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
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
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('username', 'password')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class CustomAdminAuthenticationForm(AdminAuthenticationForm):
    """
    A custom authentication form used in the admin app.
    """
    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': _(
            "Por favor introduza un nombre de usuario y contraseña correctos."
        ),
    }

    username = UsernameField(
        label='Nombre de usuario:',
        widget=forms.TextInput(attrs={'autofocus': True})
    )


class AlumnoCreationForm(forms.ModelForm):
    def generate_matricula():
        cve_uni = 61
        año = timezone.now().strftime('%y')
        last_user = Alumno.objects.last()
        if not last_user:
            return str(cve_uni) + str(año) + '00001'
        else:
            matricula = last_user.username
            consecutivo = int(matricula[-5:]) + 1
            matricula = str(cve_uni) + str(año) + str(consecutivo).zfill(5)
            return matricula

    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', initial=generate_matricula, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    password2 = forms.CharField(label='Confirmar Contraseña', initial=generate_matricula, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    username = forms.CharField(max_length=9, initial=generate_matricula, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

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
    
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Alumno
        fields = ('username', 'password')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class ProfesorCreationForm(forms.ModelForm):
    # def generate_matricula():
    #     cve_uni = 61
    #     año = timezone.now().strftime('%y')
    #     last_user = Profesor.objects.last()
    #     if not last_user:
    #         return str(cve_uni) + str(año) + '00001'
    #     else:
    #         matricula = last_user.username
    #         consecutivo = int(matricula[-5:]) + 1
    #         matricula = str(cve_uni) + str(año) + str(consecutivo).zfill(5)
    #         return matricula


    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

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


class ProfesorChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Profesor
        fields = ('username', 'password')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]