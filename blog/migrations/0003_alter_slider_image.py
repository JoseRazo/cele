# Generated by Django 3.2 on 2022-11-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_slider_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(help_text='El tamaño de la imagen debe ser de 1920 x 850 pixeles', upload_to='blog/slider_principal'),
        ),
    ]
