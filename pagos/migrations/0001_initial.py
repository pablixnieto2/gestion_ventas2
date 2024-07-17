# Generated by Django 5.0.7 on 2024-07-16 15:07

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('changetimestamp', models.DateTimeField(auto_now=True)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tienda', models.CharField(choices=[('Madrid', 'Madrid'), ('Valencia', 'Valencia'), ('Barcelona', 'Barcelona'), ('Videollamada', 'Videollamada')], default='Madrid', max_length=50)),
                ('metodo_pago', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Tarjeta', 'Tarjeta'), ('BBVA', 'BBVA'), ('SumUp', 'SumUp'), ('Bizum', 'Bizum'), ('Transferencia', 'Transferencia'), ('Paypal', 'Paypal'), ('Web', 'Web')], max_length=50)),
                ('referencia_pago', models.CharField(blank=True, max_length=50, null=True)),
                ('comentarios', models.TextField(blank=True)),
                ('estado_pago', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Pagado', 'Pagado'), ('Reembolsado', 'Reembolsado')], default='Pendiente', max_length=50)),
                ('detalles_ticket', models.TextField(blank=True)),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.venta')),
            ],
            options={
                'verbose_name_plural': 'Pagos',
            },
        ),
    ]
