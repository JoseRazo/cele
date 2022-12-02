# Generated by Django 3.2 on 2022-09-21 20:36

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuarios.usuario')),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('calle', models.CharField(blank=True, max_length=60, null=True)),
                ('num_exterior', models.CharField(blank=True, max_length=15, null=True)),
                ('num_interior', models.CharField(blank=True, max_length=15, null=True)),
                ('tipo_usuario', models.PositiveSmallIntegerField(choices=[(1, 'Estudiante UTS'), (2, 'Egresado UTS'), (3, 'Persona Externa')])),
                ('avatar', models.ImageField(blank=True, default='default.png', null=True, upload_to='avatar')),
                ('ciudad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ciudad_alumno', to='sistema.ciudad')),
                ('colonia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='colonia_alumno', to='sistema.colonia')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='estado_alumno', to='sistema.estado')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
            bases=('usuarios.usuario',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio_estudiante_uts', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Precio Estudiante UTS')),
                ('precio_persona_externa', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Precio Persona Externa')),
                ('activo', models.BooleanField(default=True)),
                ('imagen', models.ImageField(blank=True, default='default-image-curso-620x600.jpg', null=True, upload_to='cursos')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuarios.usuario')),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('avatar', models.ImageField(blank=True, default='default.png', null=True, upload_to='avatar')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
            },
            bases=('usuarios.usuario',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CursoAlumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inscrito', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_escolar.alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_escolar.curso')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_escolar.periodo')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_escolar.profesor')),
            ],
            options={
                'verbose_name': 'Curso Alumno',
                'verbose_name_plural': 'Cursos Alumnos',
            },
        ),
        migrations.CreateModel(
            name='CalificacionCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_examen', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Primer Examen')),
                ('segundo_examen', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Segundo Examen')),
                ('calificacion_final', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Calificación Final')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('curso_alumno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion_escolar.cursoalumno')),
            ],
            options={
                'verbose_name': 'Calificacion',
                'verbose_name_plural': 'Calificaciones',
            },
        ),
    ]