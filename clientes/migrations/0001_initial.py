# Generated by Django 5.0.7 on 2024-07-11 14:41

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.EmailField(max_length=254)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('fecha_fiesta', models.DateField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('prefijo', models.CharField(max_length=3)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('ubicacion', models.CharField(choices=[('Madrid', 'Madrid'), ('Valencia', 'Valencia'), ('Barcelona', 'Barcelona'), ('Videollamada', 'Videollamada')], max_length=20)),
                ('estado', models.CharField(choices=[('sin cita', 'sin cita'), ('con cita', 'con cita'), ('perdido', 'perdido'), ('eliminar cliente duplicado', 'eliminar cliente duplicado')], max_length=50)),
                ('como_nos_conocio', models.CharField(choices=[('Google', 'Google'), ('Google maps', 'Google maps'), ('Instagram', 'Instagram'), ('Facebook', 'Facebook'), ('Recomendación', 'Recomendación'), ('Milanuncios', 'Milanuncios'), ('Web', 'Web'), ('Otro', 'Otro')], max_length=20)),
                ('label_clientes', models.CharField(max_length=255)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('razon_perdida', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('vendedora', models.CharField(max_length=100)),
                ('estado_cliente', models.CharField(choices=[('ya compró', 'ya compró'), ('perdido', 'perdido')], max_length=50)),
                ('ventas_relacionadas', models.TextField()),
                ('color', models.CharField(max_length=50)),
                ('telefono2', models.CharField(max_length=15)),
                ('label_clientes2', models.CharField(max_length=255)),
                ('related_sesiones_fotos', models.TextField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalCliente',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_by', models.EmailField(max_length=254)),
                ('creation_date', models.DateTimeField(blank=True, editable=False)),
                ('fecha_fiesta', models.DateField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('prefijo', models.CharField(max_length=3)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('ubicacion', models.CharField(choices=[('Madrid', 'Madrid'), ('Valencia', 'Valencia'), ('Barcelona', 'Barcelona'), ('Videollamada', 'Videollamada')], max_length=20)),
                ('estado', models.CharField(choices=[('sin cita', 'sin cita'), ('con cita', 'con cita'), ('perdido', 'perdido'), ('eliminar cliente duplicado', 'eliminar cliente duplicado')], max_length=50)),
                ('como_nos_conocio', models.CharField(choices=[('Google', 'Google'), ('Google maps', 'Google maps'), ('Instagram', 'Instagram'), ('Facebook', 'Facebook'), ('Recomendación', 'Recomendación'), ('Milanuncios', 'Milanuncios'), ('Web', 'Web'), ('Otro', 'Otro')], max_length=20)),
                ('label_clientes', models.CharField(max_length=255)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('razon_perdida', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('vendedora', models.CharField(max_length=100)),
                ('estado_cliente', models.CharField(choices=[('ya compró', 'ya compró'), ('perdido', 'perdido')], max_length=50)),
                ('ventas_relacionadas', models.TextField()),
                ('color', models.CharField(max_length=50)),
                ('telefono2', models.CharField(max_length=15)),
                ('label_clientes2', models.CharField(max_length=255)),
                ('related_sesiones_fotos', models.TextField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical cliente',
                'verbose_name_plural': 'historical clientes',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
