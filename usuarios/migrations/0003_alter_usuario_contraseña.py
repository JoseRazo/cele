# Generated by Django 3.2 on 2023-10-17 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_contraseña'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='contraseña',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Contraseña'),
        ),
    ]
