# Generated by Django 5.0.7 on 2024-07-16 15:07

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('changetimestamp', models.DateTimeField(auto_now=True)),
                ('tienda', models.CharField(choices=[('Madrid', 'Madrid'), ('Barcelona', 'Barcelona'), ('Valencia', 'Valencia'), ('Videollamada', 'Videollamada')], default='Madrid', max_length=50)),
                ('envio_entrega', models.BooleanField(default=False)),
                ('estado_entrega', models.CharField(choices=[('Por Entregar o Enviar', 'Por Entregar o Enviar'), ('Entregado o Enviado', 'Entregado o Enviado'), ('Vestido Devuelto', 'Vestido Devuelto')], default='Por Entregar o Enviar', max_length=50)),
                ('tipo', models.CharField(choices=[('Alquiler', 'Alquiler'), ('Venta', 'Venta')], default='Venta', max_length=10)),
                ('fecha_entrega', models.DateField()),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('amount_deposito', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('estado_deposito', models.CharField(blank=True, choices=[('Pendiente de Entrega', 'Pendiente de Entrega'), ('Entregado por el Cliente', 'Entregado por el Cliente'), ('Devuelto al Cliente', 'Devuelto al Cliente')], max_length=50, null=True)),
                ('direccion', models.TextField(blank=True)),
                ('precio_envio', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_a_pagar', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_pagado', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('pendiente_de_pago', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('estado_pago', models.CharField(default='Pendiente', max_length=50)),
                ('comentarios', models.TextField(blank=True)),
                ('estado_venta', models.CharField(default='En Proceso', max_length=50)),
                ('descuento', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('motivo', models.TextField(blank=True)),
                ('devolucion', models.TextField(blank=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='ventas/pdfs/')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('productos', models.ManyToManyField(to='productos.producto')),
            ],
            options={
                'verbose_name_plural': 'Ventas',
            },
        ),
    ]
