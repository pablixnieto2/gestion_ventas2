# Generated by Django 5.0.7 on 2024-07-24 08:18

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_by', models.EmailField(max_length=254)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_fiesta', models.DateField()),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('prefijo', models.CharField(blank=True, max_length=3, null=True)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('ubicacion', models.CharField(choices=[('Madrid', 'Madrid'), ('Valencia', 'Valencia'), ('Barcelona', 'Barcelona'), ('Videollamada', 'Videollamada')], max_length=50)),
                ('estado', models.CharField(choices=[('sin cita', 'Sin Cita'), ('con cita', 'Con Cita'), ('perdido', 'Perdido'), ('eliminar cliente duplicado', 'Eliminar Cliente Duplicado')], max_length=50)),
                ('como_nos_conocio', models.CharField(choices=[('Google', 'Google'), ('Google maps', 'Google Maps'), ('Instagram', 'Instagram'), ('Facebook', 'Facebook'), ('Recomendación', 'Recomendación'), ('Milanuncios', 'Milanuncios'), ('Web', 'Web'), ('Otro', 'Otro')], max_length=50)),
                ('comentarios', models.TextField(blank=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=10)),
                ('vendedora', models.CharField(blank=True, max_length=100)),
                ('estado_cliente', models.CharField(choices=[('En Proceso de compra', 'En Proceso de compra'), ('ya compró', 'Ya Compró'), ('perdido', 'Perdido')], max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
