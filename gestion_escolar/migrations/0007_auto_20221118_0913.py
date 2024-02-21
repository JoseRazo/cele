# Generated by Django 3.2 on 2022-11-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_escolar', '0006_auto_20221115_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspirante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('mensaje', models.TextField()),
            ],
            options={
                'verbose_name': 'Aspirante',
                'verbose_name_plural': 'Aspirantes',
            },
        ),
        migrations.AlterField(
            model_name='curso',
            name='duracion',
            field=models.CharField(blank=True, help_text='Ejemplo 2 meses o 8 semanas', max_length=50, null=True, verbose_name='Duración del Curso'),
        ),
    ]
