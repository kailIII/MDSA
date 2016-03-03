# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 02:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('documentos', '0005_documento_situacion'),
        ('tipos_documentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='tipos_documento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipos_documentos.TipoDocumento'),
        ),
    ]
