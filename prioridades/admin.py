# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import Prioridad 


@admin.register(Prioridad)
class PrioridadAdmin(admin.ModelAdmin):
	class Meta:
		model = Prioridad