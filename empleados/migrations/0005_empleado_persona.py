# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 02:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
        ('empleados', '0004_empleado_ocupacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personas.Persona'),
        ),
    ]