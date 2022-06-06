from cProfile import label
from email.mime import image
from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Alumno

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    precio_estudiante_uts = models.DecimalField(_('Precio Estudiante UTS'), max_digits=6, decimal_places=2)
    precio_persona_externa = models.DecimalField(_('Precio Persona Externa'), max_digits=6, decimal_places=2)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(default='default-image-curso-620x600.jpg', upload_to='cursos', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nombre

class Nivel(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveles'

    def __str__(self):
        return self.nombre

# class InscribirAlumno(models.Model):
#     alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
#     curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
#     nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
#     inscrito = models.BooleanField(default=False)
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
#     fecha_actualizacion = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = 'Inscribir Alumno'
#         verbose_name_plural = 'Inscribir Alumnos'

#     def __str__(self):
#         return self.alumno.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=6, unique=True)
    profesor = models.ForeignKey('usuarios.Profesor', on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    aula = models.ForeignKey('Aula', on_delete=models.CASCADE)
    alumnos = models.ManyToManyField('usuarios.Alumno', related_name='grupos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return self.nombre

class Aula(models.Model):
    edificio = models.CharField(max_length=10)
    num_aula = models.CharField(_('Número de aula'), max_length=10)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'

    def __str__(self):
        return self.edificio + '-' + self.num_aula