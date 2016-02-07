# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Zona 
# Register your models here.

@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
	list_display   = ('zona',)
	list_instances = True
	search_fields  = ('zona',)

	class Meta:
		model = Zona