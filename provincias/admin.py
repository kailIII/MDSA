# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Provincia

# Register your models here.
@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
	list_display   = ('departamento','nombre', 'descripcion', 'imagen',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Provincia

#admin.site.register(Pais, PaisAdmin)