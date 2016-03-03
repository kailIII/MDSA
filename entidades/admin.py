# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Entidad
import socket

@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
	list_display   = (
					  'tipo_entidad','nombre','siglas', 'documento_identificacion', 'numero_documento_identificacion', 'email_oficial',
					  'pagina_web_oficial', 'mision', 'vision', 'logotipo', 'slug', 'descripcion', 'observacion', 'fecha_creacion', 
					  'fecha_cese', 'fecha_registro', 'usuario_creador', 'fecha_ultima_actualizacion', 'ultimo_usuario_editor',
					  'nombre_host', 'direccion_ip', 'estado',
					 )
	list_instances = True
	search_fields  = ('nombre',)
	
	exclude = ('fecha_registro','usuario_creador', 'fecha_ultima_actualizacion', 'ultimo_usuario_editor','nombre_host', 'direccion_ip' )

	def save_model(self, request, obj, form, change):
		obj.usuario_creador =  request.user
		
		try:
		    obj.nombre_host = socket.gethostname()
		except:
		    obj.nombre_host = 'localhost'

		obj.direccion_ip = socket.gethostbyname(socket.gethostname())
		
		obj.save()

	class Meta:
		model = Entidad