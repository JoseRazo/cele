# Generated by Django 3.2 on 2024-10-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_escolar', '0018_auto_20240930_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='genero',
            field=models.CharField(blank=True, choices=[('H', 'Hombre'), ('M', 'Mujer')], max_length=1, null=True),
        ),
    ]
