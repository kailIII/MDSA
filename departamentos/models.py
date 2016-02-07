# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from paises.models import Pais

# Create your models here.
class Departamento(models.Model):
	#Atributos
	pais			= models.ForeignKey(Pais, on_delete=models.CASCADE)
	nombre   		= models.CharField(max_length=255, unique=True, help_text='Escribir nombre del departamento.')
	codigo_postal  	= models.IntegerField(verbose_name='Código postal', help_text='Escribir código postal del departamento.')
	descripcion    	= models.TextField(blank=True, help_text='Escribir descripción del departamento. (Opcional)')
	imagen 		   	= models.ImageField(blank=True, upload_to='imagenes_departamentos', help_text='Subir imagen del departamento. (Opcional)')
	#slug 			= models.SlugField(max_length=255, unique=True)
	
	#Métodos
	def __unicode__(self):
		return self.nombre
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Departamentos'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Departamento' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Departamentos'