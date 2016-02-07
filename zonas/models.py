# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Zona(models.Model):
	zona = models.CharField(max_length=255, unique=True, help_text='Escribir zona.')

	#Métodos
	def __unicode__(self):
		return self.zona
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Zonas'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Zona' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Zonas'