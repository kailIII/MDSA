# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from departamentos.models import Departamento

# Create your models here.
class Provincia(models.Model):
	#Atributos
	departamento	= models.ForeignKey(Departamento, on_delete=models.CASCADE)
	nombre   		= models.CharField(max_length=255, unique=True, help_text='Escribir nombre del provincia.')
	descripcion    	= models.TextField(blank=True, help_text='Escribir descripción del provincia. (Opcional)')
	imagen 		   	= models.ImageField(blank=True, upload_to='imagenes_provincias', help_text='Subir imagen del provincia. (Opcional)')
	#slug 			= models.SlugField(max_length=255, unique=True)
	
	#Métodos
	def __unicode__(self):
		return self.nombre
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Provincias'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Provincia' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Provincias'
