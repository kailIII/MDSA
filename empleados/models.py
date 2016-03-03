# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from personas.models import Persona 
from cargos.models import Cargo 
from grados_instrucciones.models import GradoInstruccion
from tipos_empleados.models import TipoEmpleado
from profesiones.models import Profesion 
from ocupaciones.models import Ocupacion
from usuarios.models import Usuario
from estados.models import Estado 
#from codigos_barras import Codigo_Barra

from django.core.validators import validate_ipv46_address


class Empleado(models.Model):
	persona 		  				= models.OneToOneField(Persona, unique=True)
	usuario							= models.OneToOneField(Usuario, unique=True)
	tipos_empleado    				= models.ForeignKey(TipoEmpleado)
	cargo 	  				    	= models.ForeignKey(Cargo)
	grado_instruccion 				= models.ForeignKey(GradoInstruccion) 
	profesion 		  				= models.ForeignKey(Profesion)
	ocupacion 		  				= models.ForeignKey(Ocupacion)
	#codigo_barra					= models.ForeignKey(Codigo_Barra)
	#contenido_codigo_barra			= models.CharField(max_length=255, unique=True, help_text='Escribir el contenido de código de barra (Opcional).') 
	#imagen_codigo_barra			= models.ImageField(blank=True, null=True, upload_to='imagen_codigo_barra', help_text='Subir iamgen de código de barra (Opcional).')
	numero_tarjeta	  				= models.PositiveIntegerField(blank=True, help_text="Escribir el número de tarjeta. (Opcional)")
	numero_acceso_biometrico		= models.PositiveIntegerField(blank=True, help_text="Escribir el número de acceso al biométrico (Opcional)")
	fecha_inicio_contratacion 		= models.DateField(help_text="Seleccionar fecha de inicio de contratación del empleado.")
	fecha_fin_contratacion 			= models.DateField(blank=True, null=True, help_text="Seleccionar fecha de final de contratación del empleado.")
	fecha_cese						= models.DateTimeField(blank=True, null=True, help_text="Seleccionar fecha de cese del empleado.")
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True)
	descripcion		    			= models.TextField(blank=True, null=True, help_text='Escribir descripción del empleado (Opcional).')
	observacion		   				= models.TextField(blank=True, null=True, help_text='Escribir observación del empleado (Opcional).') 
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario, related_name='empleado_usuario_creador')
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='empleado_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])	#Métodos
	estado							= models.ForeignKey(Estado)

	def __unicode__(self):
		return self.persona

	#Esto es cuando en la vista no existe un commit=false
	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.persona)
		super(Empleado, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Empleados'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Empleado' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Empleados'#Métodos

	
