# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import EstadoCivil 
# Register your models here.

@admin.register(EstadoCivil)
class EstadoCivilAdmin(admin.ModelAdmin):
	list_display   = ('estado_civil',)
	list_instances = True
	search_fields  = ('estado_civil',)

	class Meta:
		model = EstadoCivil