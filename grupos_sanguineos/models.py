# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class GrupoSanguineo(models.Model):
	grupo_sanguineo = models.CharField(max_length=255, unique=True, help_text='Escribir grupo sanguíneo.')

	#Métodos
	def __unicode__(self):
		return self.grupo_sanguineo
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Grupos_Sanguineos'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Grupo Sanguineo' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Grupos Sanguineos'