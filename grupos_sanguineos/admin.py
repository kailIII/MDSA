# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import GrupoSanguineo

# Register your models here.
@admin.register(GrupoSanguineo)
class GrupoSanguineoAdmin(admin.ModelAdmin):
	list_display   = ('grupo_sanguineo',)
	list_instances = True
	search_fields  = ('grupo_sanguineo',)

	class Meta:
		model = GrupoSanguineo
