# Generated by Django 3.2 on 2023-05-16 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion_escolar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo de documento')),
                ('titulo', models.CharField(blank=True, max_length=145, null=True)),
                ('subtitulo', models.CharField(blank=True, max_length=145, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=145)),
                ('imagen', models.ImageField(upload_to='certificados')),
                ('direccion', models.CharField(blank=True, max_length=145, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Plantilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, default='default-image-certi-540x540.png', help_text='El tamaño de la imagen debe ser de 540 x 540 pixeles', null=True, upload_to='certificados')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Plantila',
                'verbose_name_plural': 'Plantillas',
                'db_table': 'certificados_plantilla',
            },
        ),
        migrations.CreateModel(
            name='DocumentoLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('imagen', models.ImageField(blank=True, default='default-image-certi-540x540.png', help_text='El tamaño de la imagen debe ser de 540 x 540 pixeles', null=True, upload_to='certificados')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificados.documento')),
            ],
            options={
                'verbose_name': 'Logo',
                'verbose_name_plural': 'Logos',
                'db_table': 'certificados_documento_logo',
            },
        ),
        migrations.CreateModel(
            name='CertificadoAlumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.CharField(blank=True, max_length=8, null=True)),
                ('firma', models.TextField()),
                ('cadena', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('curso_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_escolar.cursoalumno')),
                ('plantilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificados.plantilla')),
            ],
            options={
                'verbose_name': 'Certificado Alumno',
                'verbose_name_plural': 'Certificados Alumno',
                'db_table': 'certificados_certificado_alumno',
            },
        ),
    ]
