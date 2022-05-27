# Generated by Django 3.2.13 on 2022-05-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_auto_20220527_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='avatar',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='tipo_usuario',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Estudiante UTS'), (2, 'Egresado UTS'), (3, 'Persona Externa')]),
        ),
    ]
