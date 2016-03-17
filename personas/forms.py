# -*- encoding: utf-8 -*-
from django import forms
from .models import Persona

class PersonaModelForm(forms.ModelForm):
	class Meta:
		model  = Persona
		exclude = (
				   'fecha_registro', 'usuario_creador', 'fecha_ultima_actualizacion', 'ultimo_usuario_editor',
				   'nombre_host', 'direccion_ip',
				  )