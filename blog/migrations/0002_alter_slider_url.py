# Generated by Django 3.2 on 2022-11-10 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='URL'),
        ),
    ]
