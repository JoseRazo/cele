# Generated by Django 3.2 on 2022-06-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_escolar', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='codigo',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
