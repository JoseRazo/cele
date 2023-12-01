from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractUser):
    username = models.CharField(max_length=60, unique=True)
    contraseña = models.CharField(_('Contraseña'), max_length=9, null=True, blank=True)
    first_name = ''
    last_name = ''
    nombre = models.CharField(_('Nombres'), max_length=150)
    apellido_paterno = models.CharField(_('Apellido Paterno'), max_length=60, null=True, blank=True)
    apellido_materno = models.CharField(_('Apellido Materno'), max_length=60, null=True, blank=True)
    email = models.EmailField(_('Email'),max_length=255, unique=True)
    preferencial = models.BooleanField(_('Usuario Preferencial'), default=False, help_text="Activa esta opción solo si el usuario es Persona Externa y tiene convenio preferencial con alguna empresa.")


    def __str__(self):
        if self.apellido_paterno is None and self.apellido_materno is None:
            return f'{self.nombre}'
        elif self.apellido_paterno is None:
            return f'{self.nombre} {self.apellido_materno}'
        elif self.apellido_materno is None:
            return f'{self.nombre} {self.apellido_paterno}'
        else:
            return f'{self.nombre} {self.apellido_paterno} {self.apellido_materno}'
        
    def nombre_completo(self):
        campos_nombre = [self.nombre]
        if self.apellido_paterno:
            campos_nombre.append(self.apellido_paterno)
        if self.apellido_materno:
            campos_nombre.append(self.apellido_materno)
        return ' '.join(campos_nombre)