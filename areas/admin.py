# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import Area 
import socket

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'tipo_area', 'nombre', 'siglas', 'mision', 'vision', 'sector', 'local', 'zona', 'seccion',	  			
	'pabellon', 'edificio', 'departamento', 'piso', 'interior', 'numero', 'referencia', 'logotipo', 'anexo_telefonico', 
	'fax_interno', 'email_institucional', 'slug', 'descripcion', 'observacion','fecha_creacion', 'fecha_cese',	'fecha_registro', 
	'usuario_creador', 'fecha_ultima_actualizacion', 'ultimo_usuario_editor', 'nombre_host', 'direccion_ip', 'estado')			    
	list_instances = True
	search_fields  = ('nombre',)

	exclude = ('fecha_registro','usuario_creador', 'fecha_ultima_actualizacion', 'ultimo_usuario_editor','nombre_host', 'direccion_ip' )

	def save_model(self, request, obj, form, change):
		#obj.empleado_registra = request.empleado_registra
		
		try:
		    obj.nombre_host = socket.gethostname()
		except:
		    obj.nombre_host = 'localhost'

		obj.direccion_ip = socket.gethostbyname(socket.gethostname())
		
	class Meta:
		model = Area
