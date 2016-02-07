# -*- encoding: utf-8 -*-
from django import forms
from .models import Provincia

class ProvinciaForm(forms.ModelForm):
	class Meta:
		model  = Provincia
		fields = '__all__'
		#fields = ['nombre_pais', 'codigo_postal', 'imagen', 'descripcion']