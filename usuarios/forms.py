# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class UsuarioForm(forms.ModelForm):
	class Meta:
		model  = Usuario
		fields = '__all__'
		

class UserCreationEmailForm(UserCreationForm):
	email    = forms.EmailField()
	avatar	 = forms.ImageField()
	class Meta:
		model = Usuario 
		fields = ('username', 'email')