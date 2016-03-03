# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from distritos.models import Distrito
from empleados.models import Empleado
from entidades.models import Entidad
from estados.models import Estado
from usuarios.models import Usuario
from vias.models import Via
from zonas.models import Zona 

from django.core.validators import validate_ipv46_address

# Create your models here.
class Sede(models.Model):
	entidad 		 				= models.ForeignKey(Entidad)
	nombre 			 				= models.CharField(max_length=255, unique=True, help_text='Escribir sede.')
	persona_contacto 				= models.ForeignKey(Empleado)
	distrito		 				= models.ForeignKey(Distrito) 
	zona							= models.ForeignKey(Zona)
	via 			 				= models.ForeignKey(Via)
	nombre_direccion				= models.CharField(max_length=255, help_text="Escribir nombre de la dirección de la sede.")
	local							= models.CharField(blank=True, max_length=255, null=True, help_text='Escribir nombre del local de la sede. (Opcional).')
	pabellon						= models.CharField(blank=True, max_length=20, null=True)
	edificio						= models.CharField(blank=True, max_length=20, null=True)
	departamento					= models.CharField(blank=True, max_length=20, null=True)
	piso 							= models.CharField(blank=True, max_length=20, null=True)
	interior						= models.CharField(blank=True, max_length=20, null=True)
	numero 							= models.CharField(blank=True, max_length=20, null=True)
	cuadra							= models.CharField(blank=True, max_length=20, null=True)
	manzana							= models.CharField(blank=True, max_length=20, null=True)
	lote							= models.CharField(blank=True, max_length=20, null=True)
	sub_lote						= models.CharField(blank=True, max_length=20, null=True)
	denominacion					= models.CharField(blank=True, max_length=255, null=True, help_text="Escribir denominación (Opcional).")
	referencia						= models.CharField(blank=True, max_length=255, null=True, help_text="Escribir referencia (Opcional).")
	observacion_direccion			= models.CharField(blank=True, max_length=255, null=True, help_text="Escribir observación de la dirección (Opcional).")
	pagina_web						= models.URLField(unique=True, max_length=255, help_text='Escribir nombre de la página web de la sede (Opcional).')
	telefono						= models.PositiveIntegerField(blank=True, help_text='Escribir número de teléfono de la sede (Opcional).', default=0)
	fax								= models.PositiveIntegerField(blank=True, help_text='Escribir número de fax de la sede (Opcional).', default=0)							
	email 							= models.EmailField(unique=True, max_length=255, help_text='Escribir E-Mail de la sede (Opcional).')
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True)
	descripcion		    			= models.TextField(blank=True, null=True, help_text='Escribir descripción de la área (Opcional).')
	observacion_sede   				= models.TextField(blank=True, null=True, help_text='Escribir observación de la área (Opcional).') 
	fecha_creacion					= models.DateField(blank=True, null=True, default='01/01/1980')	
	fecha_cese						= models.DateField(blank=True, null=True)
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario)
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='sede_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])
	estado							= models.ForeignKey(Estado)

	#Métodos
	def __unicode__(self):
		return self.nombre
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Sedes'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Sede' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Sedes'#Métodos
