
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from documentos_identificaciones.models import DocumentoIdentificacion
from estados.models import Estado
from tipos_entidades.models import TipoEntidad
from usuarios.models import Usuario

from django.core.validators import validate_ipv46_address


class Entidad(models.Model):
	tipo_entidad 					= models.ForeignKey(TipoEntidad)
	nombre 					 		= models.CharField(max_length=255, unique=True, help_text='Escribir nombre de la entidad.')
	siglas							= models.CharField(max_length=25, help_text='Escribir siglas de la entidad.')
	documento_identificacion 		= models.ForeignKey(DocumentoIdentificacion)
	numero_documento_identificacion = models.PositiveIntegerField(unique=True, help_text="Escribir número documento identificación.")
	email_oficial 					= models.EmailField(unique=True, max_length=255, help_text='Escribir E-Mail de la entidad (Opcional).')
	pagina_web_oficial				= models.URLField(unique=True, max_length=255, help_text='Escribir nombre de la página web de la entidad (Opcional).')
	mision    	  			 		= models.TextField(help_text='Escribir misión de la entidad (Opcional).')
	vision 	  	  			 		= models.TextField(help_text='Escribir vision de la entidad (Opcional).')
	logotipo  	  					= models.ImageField(blank=True, null=True, upload_to='logotipo_entidad', help_text='Subir logotipo de la entidad (Opcional).')
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True)
	descripcion		    			= models.TextField(blank=True, null=True, help_text='Escribir descripción de la entidad (Opcional).')
	observacion		   				= models.TextField(blank=True, null=True, help_text='Escribir observación de la entidad (Opcional).') 
	fecha_creacion					= models.DateField(blank=True, null=True, default='01/01/1980')	
	fecha_cese						= models.DateField(blank=True, null=True)
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario)
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='entidad_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])
	estado							= models.ForeignKey(Estado)

	#Esto es cuando en la vista no existe un commit=false
	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.nombre)
		super(Entidad, self).save(*args, **kwargs)

	#Métodos
	def __unicode__(self):
		return self.nombre
		
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Entidades'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Entidad' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Entidades'#Métodos
