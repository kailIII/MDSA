# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import DocumentoIdentificacion

# Register your models here.
@admin.register(DocumentoIdentificacion)
class DocumentoIdentificacionAdmin(admin.ModelAdmin):
	list_display   = ('documento_identificacion',)
	list_instances = True
	search_fields  = ('documento_identificacion',)

	class Meta:
		model = DocumentoIdentificacion
