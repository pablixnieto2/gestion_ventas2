# Generated by Django 5.0.7 on 2024-07-13 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pagos', '0001_initial'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.venta'),
        ),
    ]
