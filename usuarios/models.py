from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractUser):
    username = models.CharField(max_length=60, unique=True)
    first_name = ''
    last_name = ''
    nombre = models.CharField(_('Nombres'), max_length=150)
    apellido_paterno = models.CharField(_('Apellido Paterno'), max_length=60, null=True, blank=True)
    apellido_materno = models.CharField(_('Apellido Materno'), max_length=60, null=True, blank=True)
    email = models.EmailField(_('Email'),max_length=255, unique=True)


    def __str__(self):
        if self.apellido_paterno is None and self.apellido_materno is None:
            return f'{self.nombre}'
        elif self.apellido_paterno is None:
            return f'{self.nombre} {self.apellido_materno}'
        elif self.apellido_materno is None:
            return f'{self.nombre} {self.apellido_paterno}'
        else:
            return f'{self.nombre} {self.apellido_paterno} {self.apellido_materno}'