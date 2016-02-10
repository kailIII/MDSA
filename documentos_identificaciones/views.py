# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import DocumentoIdentificacion
from .mixins import LoginRequiredMixin
from .forms import DocumentoIdentificacionForm
from .serializers import DocumentoIdentificacionSerializer

from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets

# Create your views here.
class DocumentoIdentificacionCreateView(CreateView):
	form_class    = DocumentoIdentificacionForm
	model 		  = DocumentoIdentificacion
	success_url   = reverse_lazy('documento_identificacion:list')
	template_name = 'documento_identificacion_create.html' 

	def get_context_data(self, **kwarg):
		context 	= super(DocumentoIdentificacionCreateView, self).get_context_data(**kwarg)
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


class DocumentoIdentificacionUpdateView(LoginRequiredMixin, UpdateView):
	form_class	  = DocumentoIdentificacionForm	
	model 		  = DocumentoIdentificacion
	queryset	  = DocumentoIdentificacion.objects.all()
	success_url   = reverse_lazy('documento_identificacion:list')
	template_name = 'documento_identificacion_update.html'

	def get_context_data(self, **kwarg):
		context  = super(DocumentoIdentificacionUpdateView, self).get_context_data(**kwarg)
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


class DocumentoIdentificacionDeleteView(LoginRequiredMixin, DeleteView):
	queryset	  = DocumentoIdentificacion.objects.all()
	model 		  = DocumentoIdentificacion
	success_url   = reverse_lazy('documento_identificacion:list')
	template_name = 'documento_identificacion_delete.html'

	def get_context_data(self, **kwarg):
		context  = super(DocumentoIdentificacionDeleteView, self).get_context_data(**kwarg)
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


class DocumentoIdentificacionDetailView(LoginRequiredMixin, DetailView):
	model 		  = DocumentoIdentificacion 
	success_url	  = reverse_lazy('documento_identificacion:list')	
	template_name = 'documento_identificacion_detail.html'

	def get_context_data(self, **kwarg):
		context 	= super(DocumentoIdentificacionDetailView, self).get_context_data(**kwarg)
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

		
class DocumentoIdentificacionListView(LoginRequiredMixin, ListView):
	model         = DocumentoIdentificacion 
	template_name = 'documento_identificacion_list.html'
	paginate_by   = 10
	def get_context_data(self, **kwarg):
		context 	= super(DocumentoIdentificacionListView, self).get_context_data(**kwarg)
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


class DocumentoIdentificacionViewSet(viewsets.ModelViewSet):
	model      		 = DocumentoIdentificacion 
	serializer_class = DocumentoIdentificacionSerializer
	queryset         = DocumentoIdentificacion.objects.all()