# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from estados.models import Estado 
from tipos_documentos.models import TipoDocumento 
from nexos.models import Nexo
from prioridades.models import Prioridad
from usuarios.models import Usuario
from situaciones.models import Situacion

from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify
import datetime


class Documento(models.Model):
	tipos_documento  				= models.ForeignKey(TipoDocumento)
	siglas							= models.CharField(max_length=25, help_text='Escribir siglas de la entidad.')
	anio			 				= models.DateTimeField(default=datetime.datetime.now())
	numero_documento 				= models.PositiveIntegerField()
	origen			 				= models.BooleanField(default=1)
	asunto 			 				= models.CharField(max_length=225, help_text='Escribir asunto del documento o Expediente (Opcional).')
	numero_folio					= models.PositiveIntegerField()
	prioridad						= models.ForeignKey(Prioridad)
	situacion						= models.ForeignKey(Situacion)
	nexo 							= models.ForeignKey(Nexo)
	fecha_recepcion 				= models.DateTimeField(default=datetime.datetime.now())
	fecha_vencimiento_procedimiento = models.DateTimeField(blank=True, null=True)
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True)
	descripcion		    			= models.TextField(blank=True, null=True, help_text='Escribir descripción del documento o Expediente (Opcional).')
	observacion		   				= models.TextField(blank=True, null=True, help_text='Escribir observación del documento o Expediente (Opcional).') 
	
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario)
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='documento_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])
	estado							= models.ForeignKey(Estado)

	def valid_extension(value):
	    if (not value.name.endswith('.png') and
	        not value.name.endswith('.jpeg') and 
	        not value.name.endswith('.gif') and
	        not value.name.endswith('.bmp') and 
	        not value.name.endswith('.jpg')):
	 
	        raise ValidationError("Archivos permitidos: .jpg, .jpeg, .png, .gif, .bmp")

	#Métodos
	def __unicode__(self):
		return self.asunto
	
	#Esto es cuando en la vista no existe un commit=false
	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.asunto)
		super(Documento, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Documentos'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Documento' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Documentos'#Métodos