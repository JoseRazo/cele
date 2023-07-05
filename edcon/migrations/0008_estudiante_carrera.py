from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_carrera'),
        ('edcon', '0007_auto_20230220_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='carrera',
            field=models.ForeignKey(blank=True, help_text='Selecciona una opción solo si es estudiante o egresado UTS', null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.carrera'),
        ),
    ]
