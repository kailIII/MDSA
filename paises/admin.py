# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Pais


# Register your models here.
@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
	list_display   = ('nombre', 'codigo_postal', 'descripcion', 'imagen',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Pais

#admin.site.register(Pais, PaisAdmin)