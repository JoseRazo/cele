from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils import timezone
from .models import Alumno

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

        # number = random.randint(00000, 99999)
        # return '61{}{}'.format(timezone.now().strftime('%y'), number)

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