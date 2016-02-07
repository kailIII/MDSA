# -*- encoding: utf-8 -*-
from django import forms
from .models import Distrito

class DistritoForm(forms.ModelForm):
	class Meta:
		model  = Distrito
		fields = '__all__'
		#fields = ['nombre_pais', 'codigo_postal', 'imagen', 'descripcion']