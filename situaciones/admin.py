# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import Situacion 


@admin.register(Situacion)
class SituacionAdmin(admin.ModelAdmin):
	class Meta:
		model = Situacion