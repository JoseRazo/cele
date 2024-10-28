# Generated by Django 3.2 on 2023-12-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_contraseña'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='preferencial',
            field=models.BooleanField(default=False, help_text='Activa esta opción solo si el usuario es Persona Externa y tiene convenio preferencial con alguna empresa.', verbose_name='Preferencial'),
        ),
    ]