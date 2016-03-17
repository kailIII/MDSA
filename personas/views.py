# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from .models import Persona
from .forms import PersonaModelForm

from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets


class PersonaTemplateView(TemplateView):
	template_name = 'persona_template.html'

	def get_context_data(self, **kwargs):
		context = super(PersonaTemplateView, self).get_context_data(**kwargs)

		is_auth  = False 
		username = None

		if self.request.user.is_authenticated():
			is_auth 	= True
			username    = self.get_username()
			
		data = {
			'is_auth'	 :is_auth,
			'username'   :username,
		}

		context.update(data)
		return context

	def get_username(self):
		return self.request.user.username

	def get_avatar(self):
		return self.request.user.get_avatar

class PersonaCreateView(CreateView):
	form_class    		= PersonaModelForm
	model 		  		= Persona
	success_url   		= reverse_lazy('persona:list')
	template_name 		= 'persona_create.html' 

	def get_context_data(self, **kwarg):
		context 	= super(PersonaCreateView, self).get_context_data(**kwarg)
		is_auth 	= False 
		username    = None
		if self.request.user.is_authenticated():
			is_auth 	= True
			username    = self.request.user.username

		data = {
			'is_auth'	 :is_auth,
			'username'   :username
		}

		context.update(data)
		return context


class PersonaUpdateView(UpdateView):
	form_class    = PersonaModelForm
	model 		  = Persona
	queryset	  = Persona.objects.all()
	success_url   = reverse_lazy('persona:list')
	template_name = 'persona_update.html'

	def get_context_data(self, **kwarg):
		context  = super(PersonaUpdateView, self).get_context_data(**kwarg)
		is_auth  = False
		username = None 
		if self.request.user.is_authenticated():
			is_auth  = True 
			username = self.request.user.username

		data = {
			'is_auth'	 :is_auth,
			'username'   :username
		}

		context.update(data)
		return context


class PersonaDeleteView(DeleteView):
	model 		  = Persona
	queryset	  = Persona.objects.all()
	success_url   = reverse_lazy('persona:list')
	template_name = 'persona_delete.html'

	def get_context_data(self, **kwarg):
		context  = super(PersonaDeleteView, self).get_context_data(**kwarg)
		is_auth  = False
		username = None 
		if self.request.user.is_authenticated():
			is_auth  = True 
			username = self.request.user.username

		data = {
			'is_auth'	 :is_auth,
			'username'   :username
		}

		context.update(data)
		return context


class PersonaDetailView(DetailView):
	model 		  = Persona
	success_url   = reverse_lazy('persona:list')
	template_name = 'persona_detail.html'

	def get_context_data(self, **kwarg):
		context 	= super(PersonaDetailView, self).get_context_data(**kwarg)
		is_auth 	= False 
		username    = None
		if self.request.user.is_authenticated():
			is_auth 	= True
			username    = self.request.user.username

		data = {
			'is_auth':is_auth,
			'username'   :username
		}

		context.update(data)
		return context

		
class PersonaListView(ListView):
	model         		= Persona 
	context_object_name = 'persona_list'
	template_name 		= 'persona_list.html'
	paginate_by   		= 10

	def get_context_data(self, **kwarg):
		context 	= super(PersonaListView, self).get_context_data(**kwarg)
		is_auth 	= False 
		username    = None
		if self.request.user.is_authenticated():
			is_auth 	= True
			username    = self.request.user.username

		data = {
			'is_auth'	 :is_auth,
			'username'   :username
		}

		context.update(data)
		return context
