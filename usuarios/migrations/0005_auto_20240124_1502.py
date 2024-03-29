# Generated by Django 3.2 on 2024-01-24 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_usuario_preferencial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='preferencial',
            field=models.BooleanField(default=False, help_text='Activa esta opción solo si el usuario es Persona Externa y tiene convenio preferencial con alguna empresa.', verbose_name='Usuario Preferencial'),
        ),
    ]
