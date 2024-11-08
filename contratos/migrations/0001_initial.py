# Generated by Django 5.1 on 2024-11-06 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='presupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_placa', models.CharField(max_length=10)),
                ('valor_p', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(unique=True)),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('nombre_u', models.CharField(max_length=50)),
                ('apellido_u', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('rol', models.CharField(choices=[('Administrador', 'Administrador'), ('Asesor', 'Asesor'), ('Logistica', 'Logística')], max_length=50)),
                ('sede', models.CharField(choices=[('Taxi Cupos', 'Taxi Cupos'), ('Green Wash', 'Green Wash')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('p_apellido', models.CharField(max_length=50)),
                ('s_apellido', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=15, unique=True)),
                ('telefono', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('barrio', models.CharField(max_length=50)),
                ('ciudad_exp', models.CharField(max_length=50)),
                ('tipo_doc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo_contratos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=10, unique=True)),
                ('marca', models.CharField(max_length=30)),
                ('linea', models.CharField(max_length=30)),
                ('modelo', models.IntegerField(null=True)),
                ('color', models.CharField(max_length=30, null=True)),
                ('cilindraje', models.CharField(max_length=30, null=True)),
                ('puertas', models.CharField(max_length=30, null=True)),
                ('capacidad', models.CharField(max_length=30, null=True)),
                ('clase', models.CharField(max_length=30, null=True)),
                ('tipo_carroceria', models.TextField(null=True)),
                ('tipo_servicio', models.TextField(null=True)),
                ('valor', models.FloatField(null=True)),
                ('n_motor', models.CharField(max_length=30, null=True)),
                ('n_chasis', models.TextField(null=True)),
                ('n_vin', models.TextField(null=True)),
                ('n_serie', models.TextField(null=True)),
                ('sitio_matricula', models.TextField(null=True)),
                ('n_acta_matricula', models.TextField(null=True)),
                ('fecha_matricula', models.DateField(null=True)),
                ('ciudad_vehiculo', models.CharField(max_length=50, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='vehiculos/')),
                ('presupuesto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contratos.presupuesto')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_factura', models.CharField(max_length=20)),
                ('nit', models.CharField(max_length=20)),
                ('nombre_local', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField()),
                ('cantidad', models.IntegerField()),
                ('valor', models.FloatField()),
                ('iva', models.BooleanField(default=False)),
                ('total', models.FloatField(null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='facturas/')),
                ('id_placa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratos.vehiculo_contratos')),
            ],
        ),
        migrations.CreateModel(
            name='estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Vitrina', 'Vitrina'), ('Taller', 'Taller'), ('Vendido', 'Vendido'), ('Chatarrizado', 'Chatarrizado')], max_length=20)),
                ('id_placa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratos.vehiculo_contratos')),
            ],
        ),
        migrations.CreateModel(
            name='documentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_orden', models.CharField(max_length=50)),
                ('emp_afiliadora', models.CharField(max_length=50)),
                ('n_tarjeta_operacion', models.CharField(max_length=50)),
                ('tarjeta_operacion', models.ImageField(blank=True, null=True, upload_to='documentos/tarjeta_op/')),
                ('fecha_inicial_to', models.DateField()),
                ('fecha_final_to', models.DateField()),
                ('fecha_inicio_soat', models.DateField()),
                ('fecha_final_soat', models.DateField()),
                ('soat', models.ImageField(blank=True, null=True, upload_to='documentos/soat/')),
                ('fecha_inicio_tecno', models.DateField()),
                ('fecha_final_tecno', models.DateField()),
                ('tecnomecanica', models.ImageField(blank=True, null=True, upload_to='documentos/tecnomecanica/')),
                ('fecha_inicio_sRC', models.DateField()),
                ('fecha_final_sRc', models.DateField()),
                ('seguros_rc', models.ImageField(blank=True, null=True, upload_to='documentos/seguros/')),
                ('id_placa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratos.vehiculo_contratos')),
            ],
        ),
        migrations.CreateModel(
            name='contrato_venta_cupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_comprador', models.CharField(max_length=50)),
                ('cc_vendedor', models.CharField(max_length=50)),
                ('valor_vCupo', models.FloatField()),
                ('primer_abono', models.FloatField()),
                ('archivos', models.FileField(upload_to='')),
                ('id_placa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratos.vehiculo_contratos')),
            ],
        ),
        migrations.CreateModel(
            name='contrato_venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_comprador', models.CharField(max_length=50)),
                ('cc_vendedor', models.CharField(max_length=50)),
                ('valor_v', models.FloatField()),
                ('primer_abono', models.FloatField()),
                ('archivos', models.FileField(upload_to='')),
                ('id_placa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratos.vehiculo_contratos')),
            ],
        ),
        migrations.CreateModel(
            name='contrato_compra_cupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_comprador', models.CharField(max_length=50)),
                ('cc_vendedor', models.CharField(max_length=50)),
                ('valor_cCupo', models.FloatField()),
                ('primer_abono', models.FloatField()),
                ('archivos', models.FileField(upload_to='')),
                ('id_placa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratos.vehiculo_contratos')),
            ],
        ),
        migrations.CreateModel(
            name='contrato_compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_comprador', models.CharField(max_length=50)),
                ('cc_vendedor', models.CharField(max_length=50)),
                ('valor_c', models.FloatField()),
                ('primer_abono', models.FloatField()),
                ('archivos', models.FileField(upload_to='')),
                ('id_placa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratos.vehiculo_contratos')),
            ],
        ),
    ]
