# Generated by Django 3.2 on 2022-11-14 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_escolar', '0003_curso_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='slug',
        ),
    ]
