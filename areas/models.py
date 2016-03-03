# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from sedes.models import Sede 
from tipos_areas.models import TipoArea 
from usuarios.models import Usuario
from estados.models import Estado

from django.core.validators import validate_ipv46_address


class Area(models.Model):
	sede   	  						= models.ForeignKey(Sede)
	tipo_area 	  					= models.ForeignKey(TipoArea)	
	nombre	  	  					= models.CharField(max_length=255, unique=True, help_text='Escribir nombre del área.')
	siglas							= models.CharField(max_length=20, help_text='Escribir siglas del área.')
	mision    	  					= models.TextField(blank=True, null=True, help_text='Escribir misión del área (Opcional).')
	vision 	  	  					= models.TextField(blank=True, null=True, help_text='Escribir vision del área (Opcional).')	
	sector							= models.CharField(blank=True, max_length=255, null=True, help_text='Escribir nombre del sector del área (Opcional).')
	local							= models.CharField(blank=True, max_length=255, null=True, help_text='Escribir nombre del local del área (Opcional).')
	zona							= models.CharField(blank=True, max_length=20, null=True)
	seccion							= models.CharField(blank=True, max_length=20, null=True)
	pabellon						= models.CharField(blank=True, max_length=20, null=True)
	edificio						= models.CharField(blank=True, max_length=20, null=True)
	departamento					= models.CharField(blank=True, max_length=20, null=True)
	piso 							= models.CharField(blank=True, max_length=20, null=True)
	interior						= models.CharField(blank=True, max_length=20, null=True)
	numero 							= models.CharField(blank=True, max_length=20, null=True)
	referencia						= models.CharField(blank=True, max_length=255, null=True, help_text="Escribir referencia (Opcional).")
	logotipo  	  					= models.ImageField(blank=True, upload_to='logotipo_area', help_text='Subir logotipo del área (Opcional).')
	anexo_telefonico				= models.PositiveIntegerField(blank=True, help_text='Escribir número de anexo telefonico del área (Opcional).', default=0)
	fax_interno						= models.PositiveIntegerField(blank=True, help_text='Escribir número de fax (Interno) del área (Opcional).', default=0)
	email_institucional 			= models.EmailField(blank=True, null=True, max_length=255, help_text='Escribir E-Mail (Opcional).')
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True)
	descripcion		    			= models.TextField(blank=True, null=True, help_text='Escribir descripción del área (Opcional).')
	observacion		   				= models.TextField(blank=True, null=True, help_text='Escribir observación del área (Opcional).') 
	fecha_creacion					= models.DateField(blank=True, null=True, default='01/01/1980')	
	fecha_cese						= models.DateField(blank=True, null=True)
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario)
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='area_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])
	estado							= models.ForeignKey(Estado)

	#Esto es cuando en la vista no existe un commit=false
	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.nombre)
		super(Area, self).save(*args, **kwargs)
		
	#Métodos
	def __unicode__(self):
		return self.nombre
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Areas'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Área' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Áreas'#Métodos
