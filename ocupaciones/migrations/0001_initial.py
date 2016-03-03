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
            name='Ocupacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Escribir nombre de la ocupaci\xf3n.', max_length=255, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('nombre_host', models.CharField(max_length=255)),
                ('direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'Ocupaciones',
                'verbose_name': 'Ocupaci\xf3n',
                'verbose_name_plural': 'Ocupaciones',
            },
        ),
    ]
