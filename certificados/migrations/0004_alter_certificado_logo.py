
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificados', '0003_auto_20230503_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificado',
            name='logo',
            field=models.ImageField(blank=True, default='default-image-certi-540x540.png', help_text='El tamaño de la imagen debe ser de 540 x 540 pixeles', null=True, upload_to='certificados'),
        ),
    ]
