# Generated by Django 3.2 on 2023-05-18 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificados', '0003_certificadoestudiante'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificadoestudiante',
            old_name='curso_estudiante',
            new_name='curso_alumno',
        ),
    ]