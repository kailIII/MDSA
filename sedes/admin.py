# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Sede


@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
	list_display   = ('entidad', 'nombre', 'persona_contacto', 'distrito', 'zona', 'via', 'nombre_direccion', 'local', 
					  'pabellon', 'edificio','departamento', 'piso', 'interior', 'numero', 'cuadra', 'manzana', 'lote', 'sub_lote', 
					  'denominacion', 'referencia', 'observacion_direccion', 'pagina_web', 'telefono', 'fax', 'email', 'slug',
					  'descripcion', 'observacion_sede', 'fecha_creacion', 'fecha_cese', 'fecha_registro', 'usuario_creador', 
					  'fecha_ultima_actualizacion', 'ultimo_usuario_editor','nombre_host', 'direccion_ip', 'estado',
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
		model = Sede

