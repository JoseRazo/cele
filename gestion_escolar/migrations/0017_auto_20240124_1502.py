# Generated by Django 3.2 on 2024-01-24 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_escolar', '0016_auto_20231201_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='avatar',
        ),
    ]