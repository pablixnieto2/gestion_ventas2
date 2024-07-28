# Generated by Django 5.0.7 on 2024-07-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sesiones_fotos', '0003_remove_sesionfoto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='sesionfoto',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]