# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuarios.models import Usuario
from bandejas.models import Bandeja 
from mensajes.models import Mensaje

from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify
import datetime


class BandejaMensaje(models.Model):
	bandeja 						= models.ForeignKey(Bandeja)
	mensaje 						= models.ForeignKey(Mensaje)
	fecha_recepcion			   		= models.DateTimeField(default=datetime.datetime.now(), null=True)
	fecha_envio			   			= models.DateTimeField(default=datetime.datetime.now(), null=True)
	enviado							= models.BooleanField(default=False)
	visto 							= models.PositiveSmallIntegerField(default=0)
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True)
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario)
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='bandeja_mensaje_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])

	#Métodos
	def __unicode__(self):
		return self.id
	
	#Esto es cuando en la vista no existe un commit=false
	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.mensaje)
		super(BandejaMensaje, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Bandejas_Mensajes'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Bandeja Mensaje' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Bandejas Mensajes'