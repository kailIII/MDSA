# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import BandejaMensaje 

@admin.register(BandejaMensaje)
class BandejaMensajeAdmin(admin.ModelAdmin):
	class Meta:
		model = BandejaMensaje