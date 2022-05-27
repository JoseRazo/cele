from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractUser):
    # ESTUDIANTE = 1
    # EGRESADO = 2
    # EXTERNO = 3
    # ROLE_CHOICES = (
    #     (ESTUDIANTE, 'Estudiante UTS'),
    #     (EGRESADO, 'Egresado UTS'),
    #     (EXTERNO, 'Persona Externa'),
    # )
    username = models.CharField(max_length=60, unique=True)
    first_name = ''
    last_name = ''
    # matricula = models.CharField(max_length=9, null=True, blank=True)
    nombre = models.CharField(_('Nombres'), max_length=150)
    apellido_paterno = models.CharField(_('Apellido Paterno'), max_length=60, null=True, blank=True)
    apellido_materno = models.CharField(_('Apellido Materno'), max_length=60, null=True, blank=True)
    email = models.EmailField(_('Email'),max_length=255, unique=True)
    # telefono = models.CharField(max_length=15, null=True, blank=True)
    # estado = models.CharField(max_length=60, null=True, blank=True)
    # ciudad = models.CharField(max_length=60, null=True, blank=True)
    # colonia = models.CharField(max_length=60, null=True, blank=True)
    # calle = models.CharField(max_length=60, null=True, blank=True)
    # num_exterior = models.CharField(max_length=15, null=True, blank=True)
    # num_interior = models.CharField(max_length=15, null=True, blank=True)
    # tipo_usuario = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    # image = models.ImageField(default='default.png', upload_to='perfil')

    # campos requeridos al momento de crear un usuario por consola
    # REQUIRED_FIELDS = ['nombre', 'apellido_paterno', 'apellido_materno', 'email']


    def __str__(self):
        return f'{self.username}'
