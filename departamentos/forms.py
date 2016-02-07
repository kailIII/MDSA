# -*- encoding: utf-8 -*-
from django import forms
from .models import Departamento

class DepartamentoForm(forms.ModelForm):
	class Meta:
		model  = Departamento
		fields = '__all__'
		#fields = ['nombre_pais', 'codigo_postal', 'imagen', 'descripcion']