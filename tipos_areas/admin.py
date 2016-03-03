# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import TipoArea


@admin.register(TipoArea)
class TipoAreaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'fecha_registro', 'usuario_creador', 'fecha_ultima_actualizacion', 'ultimo_usuario_editor', 
					'nombre_host', 'direccion_ip')			 
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = TipoArea
