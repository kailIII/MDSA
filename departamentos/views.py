# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Departamento
from .forms import DepartamentoForm
from .serializers import DepartamentoSerializer
from .mixins import AccessUserRequiredMixin

from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets

# Create your views here.
class DepartamentoCreateView(AccessUserRequiredMixin, CreateView):
	form_class    = DepartamentoForm
	models        = Departamento
	success_url   = reverse_lazy('departamento:list')
	template_name = 'departamento_create.html'

	def get_context_data(self, **kwarg):
		context  = super(DepartamentoCreateView, self).get_context_data(**kwarg)
		is_auth  = False 
		username = None
		if self.request.user.is_authenticated():
			is_auth  = True
			username = self.request.user.username

		data = {
			'is_auth' :is_auth,
			'username':username
		}

		context.update(data)
		return context


class DepartamentoUpdateView(AccessUserRequiredMixin, UpdateView):
	form_class 		= DepartamentoForm
	model 			= Departamento
	queryset		= Departamento.objects.all()
	success_url     = reverse_lazy('departamento:list')
	template_name   = 'departamento_update.html'

	def get_context_data(self, **kwarg):
		context  = super(DepartamentoUpdateView, self).get_context_data(**kwarg)
		is_auth  = False
		username = None 

		if self.request.user.is_authenticated():
			is_auth  = True
			username = self.request.user.username

		data = {
			'is_auth' :is_auth,
			'username': username
		}

		context.update(data)
		return context


class DepartamentoDeleteView(AccessUserRequiredMixin, DeleteView):
	model 		  = Departamento
	queryset	  = Departamento.objects.all()
	success_url   = reverse_lazy('departamento:list')
	template_name = 'departamento_delete.html'

	def get_context_data(self, **kwarg):
		context  = super(DepartamentoDeleteView, self).get_context_data(**kwarg)
		is_auth  = False
		username = None 

		if self.request.user.is_authenticated():
			is_auth  = True
			username = self.request.user.username

		data = {
			'is_auth' :is_auth,
			'username': username
		}

		context.update(data)
		return context


class DepartamentoDetailView(AccessUserRequiredMixin, DetailView):
	model = Departamento 
	template_name = 'departamento_detail.html'

	def get_context_data(self, **kwarg):
		context  = super(DepartamentoDetailView, self).get_context_data(**kwarg)
		is_auth  = False
		username = None 

		if self.request.user.is_authenticated():
			is_auth  = True
			username = self.request.user.username

		data = {
			'is_auth' :is_auth,
			'username': username
		}

		context.update(data)
		return context

		
class DepartamentoListView(AccessUserRequiredMixin, ListView):
	model         = Departamento 
	template_name = 'departamento_list.html'
	paginate_by   = 10
	
	def get_context_data(self, **kwarg):
		context  = super(DepartamentoListView, self).get_context_data(**kwarg)
		is_auth  = False
		username = None 

		if self.request.user.is_authenticated():
			is_auth  = True
			username = self.request.user.username

		data = {
			'is_auth' :is_auth,
			'username': username
		}

		context.update(data)
		return context


class DepartamentoViewSet(viewsets.ModelViewSet):
	model      		 = Departamento 
	serializer_class = DepartamentoSerializer
	queryset         = Departamento.objects.all()