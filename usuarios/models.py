from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from sistema.models import Estado, Ciudad, Colonia

class Usuario(AbstractUser):
    username = models.CharField(max_length=60, unique=True)
    first_name = ''
    last_name = ''
    nombre = models.CharField(_('Nombres'), max_length=150)
    apellido_paterno = models.CharField(_('Apellido Paterno'), max_length=60, null=True, blank=True)
    apellido_materno = models.CharField(_('Apellido Materno'), max_length=60, null=True, blank=True)
    email = models.EmailField(_('Email'),max_length=255, unique=True)


    def __str__(self):
        return f'{self.username}'

class Alumno(Usuario):
    ESTUDIANTE = 1
    EGRESADO = 2
    EXTERNO = 3
    ROLE_CHOICES = (
        (ESTUDIANTE, 'Estudiante UTS'),
        (EGRESADO, 'Egresado UTS'),
        (EXTERNO, 'Persona Externa'),
    )
    inscrito = models.BooleanField(default=False)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True, blank=True)
    colonia = models.ForeignKey(Colonia, on_delete=models.CASCADE, null=True, blank=True)
    calle = models.CharField(max_length=60, null=True, blank=True)
    num_exterior = models.CharField(max_length=15, null=True, blank=True)
    num_interior = models.CharField(max_length=15, null=True, blank=True)
    tipo_usuario = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    avatar = models.ImageField(default='default.png', upload_to='avatar', null=True, blank=True)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"


    def __str__(self):
        return self.nombre

class Profesor(Usuario):
    telefono = models.CharField(max_length=15, null=True, blank=True)
    avatar = models.ImageField(default='default.png', upload_to='avatar', null=True, blank=True)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"


    def __str__(self):
        return self.nombre