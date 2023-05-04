from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Logo(models.Model):
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
    
    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    logo = models.ForeignKey(Logo, on_delete=models.CASCADE,
                             null=True, blank=True)
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
    tipo = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)
    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

    def __str__(self):
        return self.tipo

class Certificado(models.Model):
    nombre = models.CharField(max_length=30, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,
                               null=True, blank=True)
    titulo = models.TextField(null=True, blank=True)
    tipo = models.ForeignKey(Documento, on_delete=models.CASCADE,
                             null=True, blank=True)
    firma = models.ImageField(
        default='default-image-certi-540x540.png', upload_to='certificados', help_text="El tamaño de la imagen debe ser de 540 x 540 pixeles", blank=True, null=True)
    sello = models.ImageField(
        default='default-image-certi-540x540.png', upload_to='certificados', help_text="El tamaño de la imagen debe ser de 540 x 540 pixeles", blank=True, null=True)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)
    class Meta:
        verbose_name = "Certificado"
        verbose_name_plural = "Certificados"

    def __str__(self):
        return self.nombre
    