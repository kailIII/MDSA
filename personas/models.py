# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from documentos_identificaciones.models import DocumentoIdentificacion
from estados_civiles.models import EstadoCivil
from grupos_sanguineos.models import GrupoSanguineo
from distritos.models import Distrito 
from zonas.models import Zona 
from vias.models import Via 

# Create your models here.
class Persona(models.Model):

	BOOL_GENERO 	 				= ((True, 'Masculino'), (False, "Femenino"))
	BOOL_HIJO 		 				= ((True, 'Si'), (False, "No"))

	apellido_paterno 		 		= models.CharField(max_length=255, help_text="Escribir apellido paterno.")
	apellido_materno 		 		= models.CharField(max_length=255, help_text="Escribir apellido materno.")
	nombre 			 		 		= models.CharField(max_length=255, help_text="Escribir nombre(s).")
	documento_identificacion 		= models.ForeignKey(DocumentoIdentificacion, on_delete=models.CASCADE)
	numero_documento_identificacion = models.PositiveIntegerField(unique=True, help_text="Escribir número documento identificación.")
	fecha_nacimiento			    = models.DateField(default="01/01/1980")
	genero 							= models.BooleanField(choices=BOOL_GENERO, default=True)
	estado_civil 					= models.ForeignKey(EstadoCivil)
	hijo							= models.BooleanField(verbose_name='¿Hijo(s)?', choices=BOOL_HIJO, default=False)
	grupo_sanguineo 				= models.ForeignKey(GrupoSanguineo)
	fotografia 						= models.ImageField(blank=True, upload_to="fotografía", help_text="Subir fotografia (Opcional).")
	observacion_persona 			= models.TextField(blank=True, help_text="Escribir observación de la persona (Opcional).")
	distrito 						= models.ForeignKey(Distrito)
	zona							= models.ForeignKey(Zona)
	via								= models.ForeignKey(Via)
	nombre_direccion				= models.CharField(max_length=255, help_text="Escribir nombre de la dirección.")
	departamento					= models.CharField(blank=True, max_length=20, null=True)
	piso							= models.CharField(blank=True, max_length=20, null=True)
	interior						= models.CharField(blank=True, max_length=20, null=True)
	numero 							= models.CharField(blank=True, max_length=20, null=True)
	cuadra							= models.CharField(blank=True, max_length=20, null=True)
	manzana							= models.CharField(blank=True, max_length=20, null=True)
	lote							= models.CharField(blank=True, max_length=20, null=True)
	sub_lote						= models.CharField(blank=True, max_length=20, null=True)
	denominacion					= models.CharField(blank=True, max_length=255, help_text="Escribir denominación (Opcional).", null=True)
	referencia						= models.CharField(blank=True, max_length=255, help_text="Escribir referencia (Opcional).", null=True)
	observacion_direccion			= models.CharField(blank=True, max_length=255, help_text="Escribir observación de la dirección (Opcional).", null=True)
	telefono_personal				= models.IntegerField(blank=True, help_text="Escribir número de teléfono personal (Opcional).", default=0)
	celular_personal				= models.IntegerField(blank=True, help_text="Escribir número de celular personal (Opcional).", default=0)
	e_mail							= models.EmailField(blank=True, max_length=255, help_text="Escribir E-Mail (Opcional).", null=True)

	def __unicode__(self):
		return self.apellido_paterno + " " + self.apellido_materno + " " + self.nombre

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Personas'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Persona' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Personas'