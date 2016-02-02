# -*- encoding: utf-8 -*-
from django import forms
from .models import Pais

class PaisForm(forms.ModelForm):
	class Meta:
		model  = Pais
		fields = '__all__'
		#fields = ['nombre_pais', 'codigo_postal', 'imagen', 'descripcion']



