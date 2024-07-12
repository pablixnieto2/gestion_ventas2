# Generated by Django 5.0.7 on 2024-07-11 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpedido',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Completado', 'Completado'), ('Cancelado', 'Cancelado')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Completado', 'Completado'), ('Cancelado', 'Cancelado')], max_length=50),
        ),
    ]