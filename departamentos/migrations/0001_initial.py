# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 02:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Escribir nombre del departamento.', max_length=255, unique=True)),
                ('codigo_postal', models.PositiveIntegerField(help_text='Escribir c\xf3digo postal del departamento.', verbose_name='C\xf3digo postal')),
                ('descripcion', models.TextField(blank=True, help_text='Escribir descripci\xf3n del departamento. (Opcional)')),
                ('imagen', models.ImageField(blank=True, help_text='Subir imagen del departamento. (Opcional)', upload_to='imagenes_departamentos')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('nombre_host', models.CharField(max_length=255)),
                ('direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'Departamentos',
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
    ]
