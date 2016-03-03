# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuarios.models import Usuario

from django.core.validators import validate_ipv46_address

class GrupoSanguineo(models.Model):
	nombre 							= models.CharField(max_length=255, unique=True, help_text='Escribir grupo sanguíneo.')
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario)
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='grupo_sanguineo_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])	#Método

	#Métodos
	def __unicode__(self):
		return self.nombre
		
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