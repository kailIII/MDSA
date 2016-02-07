# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Persona 
# Register your models here.

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
	list_display   = ('apellido_paterno','apellido_materno', 'nombre', 'documento_identificacion',
					  'numero_documento_identificacion', 'fecha_nacimiento', 'genero', 'estado_civil', 'grupo_sanguineo','fotografia',
					  'observacion_persona', 'distrito', 'zona', 'via', 'nombre_direccion', 'departamento', 'piso', 'interior', 'numero',
					  'cuadra', 'manzana', 'lote','sub_lote', 'denominacion', 'referencia', 'observacion_direccion',
					  'telefono_personal', 'celular_personal','e_mail',)
	list_instances = True
	search_fields  = ('nombre','apellido_paterno', 'apellido_materno')

	class Meta:
		model = Persona