from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=60)
    abreviatura = models.CharField(max_length=3)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=60)
    abreviatura = models.CharField(max_length=5)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=60)
    lada = models.CharField(max_length=4)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.nombre

class Colonia(models.Model):
    nombre = models.CharField(max_length=60)
    codigo_postal = models.CharField(max_length=7)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Colonia'
        verbose_name_plural = 'Colonias'

    def __str__(self):
        return self.nombre