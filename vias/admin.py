# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Via 
# Register your models here.

@admin.register(Via)
class ViaAdmin(admin.ModelAdmin):
	list_display   = ('via',)
	list_instances = True
	search_fields  = ('via',)

	class Meta:
		model = Via