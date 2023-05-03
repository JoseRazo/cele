from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

class Certificado(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    logo = models.ImageField(
        default='default-image-certi-540x540.png', upload_to='certificados', help_text="El tamaño de la imagen debe ser de 540 x 540 pixeles", blank=True, null=True)
    