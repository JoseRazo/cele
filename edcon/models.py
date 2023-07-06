from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Usuario
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
from sistema.models import Estado, Ciudad, Colonia, Carrera


# Create your models here.

class Estudiante(Usuario):
    ESTUDIANTE = 1
    EGRESADO = 2
    EXTERNO = 3
    ADMINISTRATIVO = 4
    ROLE_CHOICES = (
        (ESTUDIANTE, 'Estudiante UTS'),
        (EGRESADO, 'Egresado UTS'),
        (EXTERNO, 'Persona Externa'),
        (ADMINISTRATIVO, 'Personal Administrativo'),

    )
    telefono = models.CharField(max_length=15, null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True, related_name='estado_estudiante')
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True, blank=True, related_name='ciudad_estudiante')
    colonia = models.ForeignKey(Colonia, on_delete=models.CASCADE, null=True, blank=True, related_name='colonia_estudiante')
    calle = models.CharField(max_length=60, null=True, blank=True)
    num_exterior = models.CharField(max_length=15, null=True, blank=True)
    num_interior = models.CharField(max_length=15, null=True, blank=True)
    tipo_usuario = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, null=True, blank=True, 
                                help_text="Selecciona una opción solo si es estudiante o egresado UTS")
    avatar = models.ImageField(default='default.png', upload_to='avatar', null=True, blank=True)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"


    def __str__(self):
        if self.apellido_paterno is None and self.apellido_materno is None:
            return f'{self.nombre}'
        elif self.apellido_paterno is None:
            return f'{self.nombre} {self.apellido_materno}'
        elif self.apellido_materno is None:
            return f'{self.nombre} {self.apellido_paterno}'
        else:
            return f'{self.nombre} {self.apellido_paterno} {self.apellido_materno}'

class Instructor(Usuario):
    telefono = models.CharField(max_length=15, null=True, blank=True)
    avatar = models.ImageField(default='default.png', upload_to='avatar', null=True, blank=True)

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructores"


    def __str__(self):
        if self.apellido_paterno is None and self.apellido_materno is None:
            return f'{self.nombre}'
        elif self.apellido_paterno is None:
            return f'{self.nombre} {self.apellido_materno}'
        elif self.apellido_materno is None:
            return f'{self.nombre} {self.apellido_paterno}'
        else:
            return f'{self.nombre} {self.apellido_paterno} {self.apellido_materno}'


class Curso(models.Model):
    EDCON = 1
    REDCONOCER = 2
    CURSO_CHOICES = (
        (EDCON, 'EdCon'),
        (REDCONOCER, 'Red Conocer'),
    )
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    tipo_curso = models.PositiveSmallIntegerField(choices=CURSO_CHOICES, default=1)
    duracion = models.CharField(max_length=50, null=True, blank=True, verbose_name="Duración del Curso", help_text="Ejemplo 2 meses o 8 semanas")
    precio_estudiante_uts = models.DecimalField(_('Precio Estudiante UTS'), max_digits=6, decimal_places=2)
    precio_persona_externa = models.DecimalField(_('Precio Persona Externa'), max_digits=6, decimal_places=2)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(default='default-image-curso-770x433.png', upload_to='cursos', help_text="El tamaño de la imagen debe ser de 770 x 436 pixeles", blank=True, null=True)
    slug=models.SlugField(null=True, unique=True)
    fecha_creacion = models.DateTimeField(_('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(_('Fecha de actualización'), auto_now=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nombre

class Periodo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(_('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(_('Fecha de actualización'), auto_now=True)

    def __str__(self):
        return self.nombre

class CursoEstudiante(models.Model):
    EN_PROGRESO = 1
    COMPLETADO = 2
    NO_COMPLETADO = 3
    ESTATUS_CHOICES = (
        (EN_PROGRESO, 'En progreso'),
        (COMPLETADO, 'Completado'),
        (NO_COMPLETADO, 'No completado'),
    )

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    inscrito = models.BooleanField(default=False)
    estatus = models.PositiveSmallIntegerField(choices=ESTATUS_CHOICES, default='En progreso')
    fecha_creacion = models.DateTimeField(_('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(_('Fecha de actualización'), auto_now=True)

    class Meta:
        verbose_name = 'Curso Estudiante'
        verbose_name_plural = 'Cursos Estudiantes'

    def __str__(self):
        return self.curso.nombre
        # return self.estudiante.nombre + ' - ' + self.curso.nombre + ' - ' + self.periodo.nombre

# class CalificacionCurso(models.Model):
#     curso_estudiante = models.OneToOneField(CursoEstudiante, on_delete=models.CASCADE)
#     primer_examen = models.DecimalField(_('Primer Examen'), max_digits=6, decimal_places=2, default=0)
#     segundo_examen = models.DecimalField(_('Segundo Examen'), max_digits=6, decimal_places=2, default=0)
#     calificacion_final = models.DecimalField(_('Calificación Final'), max_digits=6, decimal_places=2, default=0)
#     fecha_creacion = models.DateTimeField(_('Fecha de creación'), auto_now_add=True)
#     fecha_actualizacion = models.DateTimeField(_('Fecha de actualización'), auto_now=True)

#     def save(self):
#         self.calificacion_final = (self.primer_examen + self.segundo_examen) / 2
#         return super(CalificacionCurso, self).save()

#     class Meta:
#         verbose_name = 'Calificacion'
#         verbose_name_plural = 'Calificaciones'
    


# class Grupo(models.Model):
#     nombre = models.CharField(max_length=100)
#     codigo = models.CharField(max_length=6, unique=True)
#     profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
#     curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
#     periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
#     aula = models.ForeignKey('Aula', on_delete=models.CASCADE)
#     estudiantes = models.ManyToManyField(Estudiante,)
#     # estudiantes = ChainedManyToManyField(
#     #     CursoEstudiante,
#     #     related_name='grupo_estudiantes',
#     #     horizontal=True,
#     #     chained_field='curso',
#     #     chained_model_field='curso',
#     # )
#     fecha_creacion = models.DateTimeField(_('Fecha de creación'), auto_now_add=True)
#     fecha_actualizacion = models.DateTimeField(_('Fecha de actualización'), auto_now=True)

#     class Meta:
#         verbose_name = 'Grupo'
#         verbose_name_plural = 'Grupos'

#     def __str__(self):
#         return self.nombre

# class Aula(models.Model):
#     edificio = models.CharField(max_length=10)
#     num_aula = models.CharField(_('Número de aula'), max_length=10)
#     fecha_creacion = models.DateTimeField(_('Fecha de creación'), auto_now_add=True)
#     fecha_actualizacion = models.DateTimeField(_('Fecha de actualización'), auto_now=True)

#     class Meta:
#         verbose_name = 'Aula'
#         verbose_name_plural = 'Aulas'

#     def __str__(self):
#         return self.edificio + '-' + self.num_aula