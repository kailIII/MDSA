# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cargos.models import Cargo
from entidades.models import Entidad
from estados.models import Estado 
from personas.models import Persona
from usuarios.models import Usuario

from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify


class Nexo(models.Model):
	persona 						= models.ForeignKey(Persona)
	entidad							= models.ForeignKey(Entidad)
	nombre_oficina					= models.CharField(blank=True, null=True, max_length=225, help_text='Escribir nombre de la oficina perteneciente (Opcional).')
	cargo							= models.ForeignKey(Cargo)
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True)
	descripcion		    			= models.TextField(blank=True, null=True, help_text='Escribir descripción del administrado (Opcional).')
	observacion		   				= models.TextField(blank=True, null=True, help_text='Escribir observación del administrado (Opcional).') 
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario)
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='nexo_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])
	estado							= models.ForeignKey(Estado)

	#Métodos
	def __unicode__(self):
		return self.persona
	
	#Esto es cuando en la vista no existe un commit=false
	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.persona)
		super(Nexo, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Nexos'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Nexo' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Nexos'#Métodos