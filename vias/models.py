# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Via(models.Model):
	via = models.CharField(max_length=255, unique=True, help_text='Escribir vía.')

	#Métodos
	def __unicode__(self):
		return self.via
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Vias'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Vía' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Vías'