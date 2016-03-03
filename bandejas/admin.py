# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import Bandeja 

@admin.register(Bandeja)
class BandejaAdmin(admin.ModelAdmin):
	class Meta:
		model = Bandeja