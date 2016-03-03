# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import Empleado 

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
	class Meta:
		model = Empleado