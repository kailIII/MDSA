# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EstadoCivil(models.Model):
	estado_civil = models.CharField(max_length=255, unique=True, help_text='Escribir estado civil.')

	#Métodos
	def __unicode__(self):
		return self.estado_civil
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Estados_Civiles'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Estado Civil' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Estados Civiles'