# Generated by Django 3.2 on 2022-10-04 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='contraseña',
            field=models.CharField(default=123456789, max_length=9, verbose_name='Contraseña'),
            preserve_default=False,
        ),
    ]
