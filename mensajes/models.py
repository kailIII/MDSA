# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from documentos.models import Documento
from estados.models import Estado 
from nexos.models import Nexo
from tipos_documentos.models import TipoDocumento 
from usuarios.models import Usuario


from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify
import datetime


class Mensaje(models.Model):
	asunto 							= models.CharField(max_length=255, unique=True, help_text='Escribir título del mensaje')
	documento 						= models.ForeignKey(Documento)
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True)
	contenido		    			= models.TextField(blank=True, null=True, help_text='Escribir contenido del mensaje (Opcional).')
	observacion		   				= models.TextField(blank=True, null=True, help_text='Escribir observación del mensaje (Opcional).') 
	usuario_emisor					= models.ForeignKey(Usuario, related_name='mensaje_usuario_emisor')
	usuario_receptor				= models.ForeignKey(Usuario, related_name='mensaje_usuario_receptor')
	
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario, related_name='mensaje_usuario_creador')
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='mensaje_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])
	estado							= models.ForeignKey(Estado)

	#Métodos
	def __unicode__(self):
		return self.asunto
	
	#Esto es cuando en la vista no existe un commit=false
	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.asunto)
		super(Mensaje, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Mensajes'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Mensaje' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Mensajes'#Métodos