# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.CharField(help_text='Escribir zona.', max_length=255, unique=True)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'Zonas',
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
            },
        ),
    ]
