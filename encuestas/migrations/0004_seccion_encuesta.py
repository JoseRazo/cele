# Generated by Django 3.2 on 2023-06-22 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0003_pregunta_seccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='seccion',
            name='encuesta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuestas.encuesta'),
        ),
    ]
