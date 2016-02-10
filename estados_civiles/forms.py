# -*- encoding: utf-8 -*-
from django import forms
from .models import EstadoCivil

class EstadoCivilForm(forms.ModelForm):
	class Meta:
		model  = EstadoCivil 
		fields = '__all__'