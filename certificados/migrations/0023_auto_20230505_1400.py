# Generated by Django 3.2 on 2023-05-05 19:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('certificados', '0022_auto_20230504_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('imagen', models.ImageField(blank=True, default='default-image-certi-540x540.png', help_text='El tamaño de la imagen debe ser de 540 x 540 pixeles', null=True, upload_to='certificados')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Logo',
                'verbose_name_plural': 'Logos',
                'db_table': 'certificados_documento_logo',
            },
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='logo',
        ),
        migrations.AddField(
            model_name='documento',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=145, null=True),
        ),
        migrations.AddField(
            model_name='documento',
            name='titulo',
            field=models.CharField(blank=True, max_length=145, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='direccion',
            field=models.CharField(blank=True, max_length=145, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='certificados'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documento',
            name='tipo',
            field=models.CharField(max_length=50, verbose_name='Tipo de documento'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombre',
            field=models.CharField(default=1, max_length=145),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Certificado',
        ),
        migrations.DeleteModel(
            name='Logo',
        ),
        migrations.AddField(
            model_name='documentologo',
            name='documento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificados.documento'),
        ),
    ]