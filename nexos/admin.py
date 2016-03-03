# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import Nexo 


@admin.register(Nexo)
class NexoAdmin(admin.ModelAdmin):
	list_display   = (
					  'persona','entidad', 'nombre_oficina', 'cargo',
					  'slug', 'descripcion', 'observacion', 
  					  'fecha_registro', 'usuario_creador', 
  					  'fecha_ultima_actualizacion', 'ultimo_usuario_editor',
  					  'nombre_host', 'direccion_ip', 'estado',
  					 )
  
	list_instances = True
	search_fields  = ('persona','entidad',)

	class Meta:
		model = Nexo