# Generated by Django 3.2 on 2023-06-26 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificados', '0004_auto_20230626_1005'),
        ('encuestas', '0006_rename_pregunta_opcion_preguntas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuesta',
            name='encuesta',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='opcion',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='pregunta',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Opcion',
        ),
        migrations.DeleteModel(
            name='Respuesta',
        ),
    ]