# -*- encoding: utf-8 -*-
from django.contrib import admin
from paises.models import Pais
from .models import Departamento

# Register your models here.
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
	list_display   = ('pais', 'nombre', 'codigo_postal', 'descripcion', 'imagen',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Departamento
