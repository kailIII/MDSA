# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Distrito

# Register your models here.
@admin.register(Distrito)
class DistritoAdmin(admin.ModelAdmin):
	list_display   = ('provincia', 'nombre', 'descripcion', 'imagen',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Distrito

#admin.site.register(Pais, PaisAdmin)
