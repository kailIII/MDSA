# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 22:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Escribir nombre del provincia.', max_length=255, unique=True)),
                ('descripcion', models.TextField(blank=True, help_text='Escribir descripci\xf3n del provincia. (Opcional)')),
                ('imagen', models.ImageField(blank=True, help_text='Subir imagen del provincia. (Opcional)', upload_to='imagenes_provincias')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamentos.Departamento')),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'Provincias',
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
            },
        ),
    ]