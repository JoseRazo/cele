# Generated by Django 3.2 on 2022-10-08 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenciasBanco',
            fields=[
                ('cve_referencia', models.BigAutoField(primary_key=True, serialize=False)),
                ('concepto', models.CharField(blank=True, max_length=255, null=True)),
                ('matricula', models.CharField(blank=True, max_length=255, null=True)),
                ('accion', models.CharField(blank=True, max_length=255, null=True)),
                ('referencia', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('banco_emisor', models.CharField(blank=True, max_length=255, null=True)),
                ('servicio_bb', models.CharField(blank=True, max_length=255, null=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=8)),
                ('forma_pago', models.CharField(blank=True, max_length=255, null=True)),
                ('monto_parcial_minimo', models.DecimalField(decimal_places=2, max_digits=8)),
                ('firma', models.TextField(blank=True, null=True)),
                ('estatus', models.CharField(blank=True, max_length=255, null=True)),
                ('mensaje', models.CharField(blank=True, max_length=255, null=True)),
                ('monto_original', models.DecimalField(decimal_places=2, max_digits=8)),
                ('recargo_aplicado', models.DecimalField(decimal_places=2, max_digits=8)),
                ('descuento_aplicado', models.DecimalField(decimal_places=2, max_digits=8)),
                ('monto_a_pagar', models.DecimalField(decimal_places=2, max_digits=8)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('no_recibo', models.CharField(blank=True, max_length=255, null=True)),
                ('folio_pago', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_limite_pago', models.CharField(blank=True, max_length=10, null=True)),
                ('fecha_pago', models.CharField(blank=True, max_length=10, null=True)),
                ('hora_pago', models.CharField(blank=True, max_length=16, null=True)),
                ('folio_reverso', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_reverso', models.CharField(blank=True, max_length=10, null=True)),
                ('hora_reverso', models.CharField(blank=True, max_length=16, null=True)),
                ('cve_periodo', models.IntegerField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField()),
                ('fecha_actualizacion', models.DateTimeField()),
            ],
            options={
                'db_table': 'referencias_banco',
                'managed': False,
            },
        ),
    ]
