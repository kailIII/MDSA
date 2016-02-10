# -*- encoding: utf-8 -*-
from django import forms
from .models import DocumentoIdentificacion

class DocumentoIdentificacionForm(forms.ModelForm):
	class Meta:
		model  = DocumentoIdentificacion
		fields = '__all__'