# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pais(models.Model):
	#Atributos
	nombre   		= models.CharField(max_length=255, unique=True, help_text='Escribir nombre del país.')
	codigo_postal  	= models.IntegerField(verbose_name='Código postal')
	descripcion    	= models.TextField(blank=True, help_text='Escribir descripción del país. (Opcional)')
	imagen 		   	= models.ImageField(blank=True, upload_to='imagenes_paises', help_text='Subir imagen del país. (Opcional)')
	#slug 			= models.SlugField(max_length=255, unique=True)
	
	#Métodos
	def __unicode__(self):
		return self.nombre
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Paises'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'País' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Paises'