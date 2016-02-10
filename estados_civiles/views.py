# -*-encoding: utf- -*-
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import EstadoCivil
from .mixins import LoginRequiredMixin
#from braces import views
from .forms import EstadoCivilForm
from .serializers import EstadoCivilSerializer

from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets

# Create your views here.
class EstadoCivilCreateView(LoginRequiredMixin, CreateView):
	form_class	  = EstadoCivilForm 
	template_name = 'estado_civil_create.html'
	success_url   = reverse_lazy('estado_civil:list')
	model 		  = EstadoCivil 

	def get_context_data(self, **kwarg):
		context  = super(EstadoCivilCreateView, self).get_context_data(**kwarg)
		is_auth  = False
		username = None 

		if self.request.user.is_authenticated():
			is_auth  = True 
			username = self.request.user.username

		data = {
			'is_auth' :is_auth,
			'username': username
		}

		context.update(context)
		return context


class EstadoCivilUpdateView(UpdateView):
	form_class    = EstadoCivilForm
	model 	      = EstadoCivil
	queryset      = EstadoCivil.objects.all()
	success_url   = reverse_lazy('estado_civil:list')
	template_name = 'estado_civil_update.html'

	def get_context_data(self, **kwarg):
		context  = super(EstadoCivilUpdateView, self).get_context_data(**kwarg)
		is_auth  = False
		username = None 

		if self.request.user.is_authenticated():
			is_auth  = True 
			username = self.request.user.username

		data = {
			'is_auth' :is_auth,
			'username': username
		}

		context.update(context)
		return context