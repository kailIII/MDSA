# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DocumentoIdentificacion(models.Model):
	documento_identificacion = models.CharField(max_length=255, unique=True, help_text='Escribir documento de identificación.')

	#Métodos
	def __unicode__(self):
		return self.documento_identificacion
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Documentos_Identificaciones'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Documento Identificación' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Documentos Identificaciones'