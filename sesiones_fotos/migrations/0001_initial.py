# Generated by Django 5.0.7 on 2024-07-11 14:41

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ventas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalSesionFotos',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('id_sesion', models.CharField(db_index=True, max_length=6)),
                ('fecha_sesion', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('ubicacion', models.CharField(max_length=100)),
                ('fotografo', models.CharField(max_length=100)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Completada', 'Completada'), ('Cancelada', 'Cancelada')], max_length=50)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('venta', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ventas.venta')),
            ],
            options={
                'verbose_name': 'historical sesion fotos',
                'verbose_name_plural': 'historical sesion fotoss',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='SesionFotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sesion', models.CharField(max_length=6, unique=True)),
                ('fecha_sesion', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('ubicacion', models.CharField(max_length=100)),
                ('fotografo', models.CharField(max_length=100)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Completada', 'Completada'), ('Cancelada', 'Cancelada')], max_length=50)),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sesiones_fotos', to='ventas.venta')),
            ],
        ),
    ]
