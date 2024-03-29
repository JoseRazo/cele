# Generated by Django 3.2 on 2023-12-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0004_referenciasconceptosbanco_referenciasserviciosbanco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('cve_periodo', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('fecha_inicio_clases', models.DateTimeField()),
                ('fecha_fin_clases', models.DateTimeField()),
                ('numero_periodo', models.IntegerField()),
                ('no_extras', models.IntegerField(blank=True, null=True)),
                ('activo', models.BooleanField()),
            ],
            options={
                'db_table': 'periodo',
                'managed': False,
            },
        ),
    ]
