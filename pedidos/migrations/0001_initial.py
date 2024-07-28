# Generated by Django 5.0.7 on 2024-07-26 18:30

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'PedidoProductos',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('changetimestamp', models.DateTimeField(auto_now=True)),
                ('estado_pedido', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Procesando', 'Procesando'), ('Completado', 'Completado'), ('Cancelado', 'Cancelado')], max_length=50)),
                ('comentarios', models.TextField(blank=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
            options={
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
