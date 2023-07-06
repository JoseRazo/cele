from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from usuarios.models import Usuario
from gestion_escolar.models import CursoAlumno
from edcon.models import CursoEstudiante

# Create your models here.
class Encuesta(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = RichTextField(_('Descripción'), null=True, blank=True)
    activo = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)

    class Meta:
        verbose_name = "Encuesta"
        verbose_name_plural = "Encuestas"
        db_table = 'encuestas_encuesta'

    def __str__(self):
        return self.nombre

class Seccion(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)

    class Meta:
        verbose_name = "Sección"
        verbose_name_plural = "Secciones"

    def __str__(self):
        return self.nombre
    
class TipoPregunta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)

    class Meta:
        verbose_name = "Tipo de Pregunta"
        verbose_name_plural = "Tipo de Preguntas"
        db_table = 'encuestas_tipo_pregunta'

    def __str__(self):
        return self.nombre
    
class Pregunta(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    tipo_pregunta = models.ForeignKey(TipoPregunta, on_delete=models.CASCADE)
    texto_pregunta = models.CharField('Texto de la pregunta', max_length=245)
    texto_ayuda = RichTextField(_('Texto de ayuda'), null=True, blank=True)
    activo = models.BooleanField(default=True)
    requerido = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)
    
    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"
        db_table = 'encuestas_pregunta'

    def __str__(self):
        return self.texto_pregunta
    
class RegistrosCELE(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso_alumno = models.ForeignKey(CursoAlumno, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)

    class Meta:
        verbose_name = "Registro CELE"
        verbose_name_plural = "Registros CELE"

    def __str__(self):
        return str(self.usuario)

class RegistrosEDCON(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso_alumno = models.ForeignKey(CursoEstudiante, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)

    class Meta:
        verbose_name = "Registro EDCON"
        verbose_name_plural = "Registros EDCON"

    def __str__(self):
        return str(self.usuario)
    
class EncuestaAlumno(models.Model):
    curso_alumno = models.ForeignKey(CursoAlumno, on_delete=models.CASCADE)
    registro = models.ForeignKey(RegistrosCELE, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_respuesta = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Encuesta de Evalución del Servicio CELE"
        verbose_name_plural = "Encuestas de Evaluación del Servicio CELE"

    def __str__(self):
        return f"{self.curso_alumno} - {self.encuesta} - {self.pregunta}"

class EncuestaEstudiante(models.Model):
    curso_alumno = models.ForeignKey(CursoEstudiante, on_delete=models.CASCADE)
    registro = models.ForeignKey(RegistrosEDCON, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_respuesta = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Encuesta de Evalución del Servicio EDCON"
        verbose_name_plural = "Encuestas de Evaluación del Servicio EDCON"

    def __str__(self):
        return f"{self.curso_alumno} - {self.encuesta} - {self.pregunta}"