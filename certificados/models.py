from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

class Documento(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

class Certificado(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    titulo = models.TextField(null=True, blank=True)
    firma = models.ImageField(
        default='default-image-certi-540x540.png', upload_to='certificados', help_text="El tamaño de la imagen debe ser de 540 x 540 pixeles", blank=True, null=True)
    sello = models.ImageField(
        default='default-image-certi-540x540.png', upload_to='certificados', help_text="El tamaño de la imagen debe ser de 540 x 540 pixeles", blank=True, null=True)
    class Meta:
        verbose_name = "Certificado"
        verbose_name_plural = "Certificados"

class Logo(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    imagen = models.ImageField(
        default='default-image-certi-540x540.png', upload_to='certificados', help_text="El tamaño de la imagen debe ser de 540 x 540 pixeles", blank=True, null=True)
    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logos"
    