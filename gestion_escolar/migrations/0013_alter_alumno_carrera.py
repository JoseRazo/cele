# Generated by Django 3.2 on 2023-05-22 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_carrera'),
        ('gestion_escolar', '0012_alter_curso_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='carrera',
            field=models.ForeignKey(blank=True, help_text='Selecciona una opción solo si es estudiante o egresado UTS', null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.carrera'),
        ),
    ]
