# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Provincia
from .mixins import LoginRequiredMixin
from .forms import ProvinciaForm
from .serializers import ProvinciaSerializer

from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets

# Create your views here.
class ProvinciaCreateView(LoginRequiredMixin, CreateView):
	form_class    = ProvinciaForm
	models        = Provincia
	success_url   = reverse_lazy('provincia:list')
	template_name = 'provincia_create.html'

	def get_context_data(self, **kwarg):
		context 	= super(ProvinciaCreateView, self).get_context_data(**kwarg)
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


class ProvinciaUpdateView(LoginRequiredMixin, UpdateView):
	form_class	  = ProvinciaForm	
	model 		  = Provincia
	queryset	  = Provincia.objects.all()
	success_url   = reverse_lazy('provincia:list')
	template_name = 'provincia_update.html'

	def get_context_data(self, **kwarg):
		context  = super(ProvinciaUpdateView, self).get_context_data(**kwarg)
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


class ProvinciaDeleteView(LoginRequiredMixin, DeleteView):
	queryset	  = Provincia.objects.all()
	model 		  = Provincia
	success_url   = reverse_lazy('provincia:list')
	template_name = 'provincia_delete.html'

	def get_context_data(self, **kwarg):
		context  = super(ProvinciaDeleteView, self).get_context_data(**kwarg)
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


class ProvinciaDetailView(LoginRequiredMixin, DetailView):
	model 		  = Provincia 
	success_url	  = reverse_lazy('provincia:list')	
	template_name = 'provincia_detail.html'

	def get_context_data(self, **kwarg):
		context 	= super(ProvinciaDetailView, self).get_context_data(**kwarg)
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

		
class ProvinciaListView(LoginRequiredMixin, ListView):
	model         = Provincia 
	template_name = 'provincia_list.html'
	paginate_by   = 10
	def get_context_data(self, **kwarg):
		context 	= super(ProvinciaListView, self).get_context_data(**kwarg)
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


class ProvinciaViewSet(viewsets.ModelViewSet):
	model      		 = Provincia 
	serializer_class = ProvinciaSerializer
	queryset         = Provincia.objects.all()