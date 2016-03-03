# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import Mensaje 

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
	class Meta:
		model = Mensaje