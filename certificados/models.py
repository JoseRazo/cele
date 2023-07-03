from django.db import models
from django.utils.translation import gettext_lazy as _
from gestion_escolar.models import CursoAlumno
from edcon.models import CursoEstudiante
from encuestas.models import Encuesta, Pregunta

# Create your models here.

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=145)
    imagen = models.ImageField(upload_to='certificados')
    direccion = models.CharField(max_length=145, null=True, blank=True)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nombre
    
class Documento(models.Model):
    tipo = models.CharField(_('Tipo de documento'), max_length=50)
    titulo = models.CharField(max_length=145, null=True, blank=True)
    subtitulo = models.CharField(max_length=145, null=True, blank=True)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)
    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

    def __str__(self):
        return self.tipo

class DocumentoLogo(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE,)
    nombre = models.CharField(max_length=30, unique=True)
    imagen = models.ImageField(
        default='default-image-certi-540x540.png', upload_to='certificados', help_text="El tamaño de la imagen debe ser de 540 x 540 pixeles", blank=True, null=True)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)
    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logos"
        db_table = 'certificados_documento_logo'
    
    def __str__(self):
        return self.nombre

class Plantilla(models.Model):
    CONSTANCIA = 'Constancia UTS'
    RED_CONOCER = 'Constancia Red Conocer'
    CEDULA = 'Cédula de Acreditación'
    RECONOCIMIENTO = 'Reconocimiento UTS'
    PLANTILLA_CHOICES = (
        (CONSTANCIA, 'Constancia UTS'),
        (RED_CONOCER, 'Constancia Red Conocer'),
        (CEDULA, 'Cédula de Acreditación'),
        (RECONOCIMIENTO, 'Reconocimiento UTS'),
    )
    nombre = models.CharField(max_length=30, null=True, blank=True)
    tipo_plantilla = models.CharField(_('Tipo de Plantilla'), max_length=30, choices=PLANTILLA_CHOICES, default='Constancia UTS')
    plantilla_con_firma = models.ImageField(_('Plantilla con Firma'),
        default='default-image-certi-850x1100.png', upload_to='certificados', help_text="El tamaño de la imagen debe estar en múltiplos de 850 x 1100 pixeles")
    plantilla_sin_firma = models.ImageField(_('Plantilla sin Firma'),
        default='default-image-certi-850x1100.png', upload_to='certificados', help_text="El tamaño de la imagen debe estar en múltiplos de 850 x 1100 pixeles")
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)
    
    class Meta:
        verbose_name = "Plantila"
        verbose_name_plural = "Plantillas"
        db_table = 'certificados_plantilla'

    def __str__(self):
        return str(self.nombre)


class CertificadoAlumno(models.Model):
    curso_alumno = models.ForeignKey(CursoAlumno, on_delete=models.CASCADE)
    plantilla = models.ForeignKey(Plantilla, on_delete=models.CASCADE)
    folio = models.CharField(max_length=20, null=True, blank=True)
    firma = models.TextField()
    cadena = models.TextField()
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)
    
    class Meta:
        verbose_name = "Certificado Alumno"
        verbose_name_plural = "Certificados Alumno"
        db_table = 'certificados_certificado_alumno'
    
    # def __str__(self):
    #     return self.curso_alumno.curso

class CertificadoEstudiante(models.Model):
    curso_alumno = models.ForeignKey(CursoEstudiante, on_delete=models.CASCADE)
    plantilla = models.ForeignKey(Plantilla, on_delete=models.CASCADE)
    folio = models.CharField(max_length=20, null=True, blank=True)
    firma = models.TextField()
    cadena = models.TextField()
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)
    
    class Meta:
        verbose_name = "Certificado Estudiante"
        verbose_name_plural = "Certificados Estudiante"
        db_table = 'certificados_certificado_estudiante'