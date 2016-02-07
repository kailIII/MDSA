# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from provincias.models import Provincia

# Create your models here.
class Distrito(models.Model):
	#Atributos
	provincia		= models.ForeignKey(Provincia, on_delete=models.CASCADE)
	nombre   		= models.CharField(max_length=255, unique=True, help_text='Escribir nombre del distrito.')
	descripcion    	= models.TextField(blank=True, help_text='Escribir descripción del distrito. (Opcional)')
	imagen 		   	= models.ImageField(blank=True, upload_to='imagenes_provincias', help_text='Subir imagen del distrito. (Opcional)')
	#slug 			= models.SlugField(max_length=255, unique=True)
	
	#Métodos
	def __unicode__(self):
		return self.nombre
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Distritos'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Distrito' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Distritos'

