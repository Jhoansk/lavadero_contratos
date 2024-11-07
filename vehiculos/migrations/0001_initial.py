# Generated by Django 5.1 on 2024-11-05 09:58

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import vehiculos.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bahia',
            fields=[
                ('cod_bahia', models.AutoField(primary_key=True, serialize=False)),
                ('numero_bahia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cedula', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('s_nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('apellido', models.CharField(max_length=100)),
                ('s_apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('celular', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('cod_convenio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('placa', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=100)),
                ('linea', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_vehiculo', models.CharField(choices=[('Automovil', 'Automóvil'), ('Moto', 'Moto'), ('Taxi', 'Taxi'), ('Camioneta', 'Camioneta'), ('Pick-up', 'Pick-up'), ('Furgon', 'Furgón')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rol', models.CharField(blank=True, max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('cod_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('s_nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('apellido', models.CharField(max_length=100)),
                ('s_apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=255)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('tipo_lavado', models.CharField(max_length=100)),
                ('tiempo', models.TimeField()),
                ('valor', models.FloatField()),
                ('imagen_1', models.ImageField(null=True, upload_to=vehiculos.models.get_image_upload_path)),
                ('imagen_2', models.ImageField(null=True, upload_to=vehiculos.models.get_image_upload_path)),
                ('imagen_3', models.ImageField(null=True, upload_to=vehiculos.models.get_image_upload_path)),
                ('imagen_4', models.ImageField(null=True, upload_to=vehiculos.models.get_image_upload_path)),
                ('estado', models.CharField(default='En Espera', max_length=50)),
                ('encargado_1', models.CharField(default='Sin Asignar', max_length=100)),
                ('encargado_2', models.CharField(default='Sin Asignar', max_length=100)),
                ('en_lavado', models.BooleanField(default=False)),
                ('inicio_lavado', models.DateTimeField(blank=True, null=True)),
                ('turno', models.PositiveIntegerField(default=0)),
                ('cliente_vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.cliente')),
                ('convenio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehiculos.convenio')),
                ('placa_vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Lavado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('bahia_vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.bahia')),
                ('cliente_vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.cliente')),
                ('empleado_encargado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.empleado')),
                ('placa_vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('tipo_lavado', models.CharField(max_length=100)),
                ('tiempo', models.TimeField()),
                ('valor', models.FloatField()),
                ('imagen_1', models.ImageField(null=True, upload_to=vehiculos.models.get_image_upload_path)),
                ('imagen_2', models.ImageField(null=True, upload_to=vehiculos.models.get_image_upload_path)),
                ('imagen_3', models.ImageField(null=True, upload_to=vehiculos.models.get_image_upload_path)),
                ('imagen_4', models.ImageField(null=True, upload_to=vehiculos.models.get_image_upload_path)),
                ('estado', models.CharField(default='En Espera', max_length=50)),
                ('encargado_1', models.CharField(default='Sin Asignar', max_length=100)),
                ('encargado_2', models.CharField(default='Sin Asignar', max_length=100)),
                ('en_lavado', models.BooleanField(default=False)),
                ('inicio_lavado', models.DateTimeField(blank=True, null=True)),
                ('turno', models.PositiveIntegerField(default=0)),
                ('cliente_vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.cliente')),
                ('convenio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehiculos.convenio')),
                ('placa_vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehiculo')),
            ],
        ),
    ]
