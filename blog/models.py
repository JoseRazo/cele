from django.db import models

# Create your models here.

class Slider(models.Model):
    categoria = models.ForeignKey('CategoriaSlider', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200, null=True, blank=True)
    subtitulo = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='blog/slider_principal', help_text="El tamaño de la imagen debe ser de 1920 x 850 pixeles")
    url = models.CharField(max_length=200, null=True, blank=True, verbose_name='URL')
    activo = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'

    def __str__(self):
        return self.titulo

class CategoriaSlider(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Categoria Slider'
        verbose_name_plural = 'Categorias Sliders'

    def __str__(self):
        return self.nombre