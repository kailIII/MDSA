# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 02:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paises', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='ultimo_usuario_editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pais_usuario_editor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pais',
            name='usuario_creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
