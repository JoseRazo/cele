# Generated by Django 3.2 on 2023-06-28 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0013_registroscele_registrosedcon'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RegistrosCELE',
        ),
        migrations.DeleteModel(
            name='RegistrosEDCON',
        ),
    ]
