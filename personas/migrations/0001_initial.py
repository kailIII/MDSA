# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 02:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estados', '0001_initial'),
        ('estados_civiles', '0001_initial'),
        ('documentos_identificaciones', '0001_initial'),
        ('distritos', '0001_initial'),
        ('grupos_sanguineos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido_paterno', models.CharField(help_text='Escribir apellido paterno.', max_length=255)),
                ('apellido_materno', models.CharField(help_text='Escribir apellido materno.', max_length=255)),
                ('nombre', models.CharField(help_text='Escribir nombre(s).', max_length=255)),
                ('numero_documento_identificacion', models.PositiveIntegerField(help_text='Escribir n\xfamero documento identificaci\xf3n.', unique=True)),
                ('fecha_nacimiento', models.DateField(default='01/01/1980')),
                ('genero', models.BooleanField(choices=[(True, 'Masculino'), (False, 'Femenino')], default=True)),
                ('hijo', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=False, verbose_name='\xbfHijo(s)?')),
                ('fotografia', models.ImageField(blank=True, help_text='Subir fotografia (Opcional).', upload_to='fotograf\xeda')),
                ('observacion_persona', models.TextField(blank=True, help_text='Escribir observaci\xf3n de la persona (Opcional).')),
                ('nombre_direccion', models.CharField(help_text='Escribir nombre de la direcci\xf3n.', max_length=255)),
                ('edificio', models.CharField(blank=True, max_length=20, null=True)),
                ('apartamento', models.CharField(blank=True, max_length=20, null=True)),
                ('departamento', models.CharField(blank=True, max_length=20, null=True)),
                ('piso', models.CharField(blank=True, max_length=20, null=True)),
                ('interior', models.CharField(blank=True, max_length=20, null=True)),
                ('numero', models.CharField(blank=True, max_length=20, null=True)),
                ('cuadra', models.CharField(blank=True, max_length=20, null=True)),
                ('manzana', models.CharField(blank=True, max_length=20, null=True)),
                ('lote', models.CharField(blank=True, max_length=20, null=True)),
                ('sub_lote', models.CharField(blank=True, max_length=20, null=True)),
                ('denominacion', models.CharField(blank=True, help_text='Escribir denominaci\xf3n (Opcional).', max_length=255, null=True)),
                ('referencia', models.CharField(blank=True, help_text='Escribir referencia (Opcional).', max_length=255, null=True)),
                ('observacion_direccion', models.CharField(blank=True, help_text='Escribir observaci\xf3n de la direcci\xf3n (Opcional).', max_length=255, null=True)),
                ('telefono_personal', models.PositiveIntegerField(blank=True, default=0, help_text='Escribir n\xfamero de tel\xe9fono personal (Opcional).')),
                ('celular_personal', models.PositiveIntegerField(blank=True, default=0, help_text='Escribir n\xfamero de celular personal (Opcional).')),
                ('email', models.EmailField(blank=True, help_text='Escribir E-Mail (Opcional).', max_length=255, null=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('nombre_host', models.CharField(max_length=255)),
                ('direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distritos.Distrito')),
                ('documento_identificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos_identificaciones.DocumentoIdentificacion')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estados.Estado')),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estados_civiles.EstadoCivil')),
                ('grupo_sanguineo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_sanguineos.GrupoSanguineo')),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'Personas',
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]
