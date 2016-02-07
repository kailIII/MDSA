# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Pais
from .forms import PaisForm
from .serializers import PaisSerializer

from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets


# Create your views here.
class PaisCreateView(CreateView):
	form_class    = PaisForm
	models        = Pais
	success_url   = reverse_lazy('pais:list')
	template_name = 'pais_create.html'

	def get_context_data(self, **kwarg):
		context = super(PaisCreateView, self).get_context_data(**kwarg)
		is_auth = False 
		name    = None
		if self.request.user.is_authenticated():
			is_auth = True
			name    = self.request.user.username

		data = {
			'is_auth':is_auth,
			'name'   :name
		}

		context.update(data)
		return context


class PaisUpdateView(UpdateView):
	form_class    = PaisForm
	models        = Pais
	success_url   = reverse_lazy('pais:list')
	template_name = 'pais_update.html'
	queryset	  = Pais.objects.all()

	def get_context_data(self, **kwarg):
		context = super(PaisUpdateView, self).get_context_data(**kwarg)
		is_auth = False 
		name    = None
		if self.request.user.is_authenticated():
			is_auth = True
			name    = self.request.user.username

		data = {
			'is_auth':is_auth,
			'name'   :name
		}

		context.update(data)
		return context


class PaisDeleteView(DeleteView):
	models        = Pais
	queryset	  = Pais.objects.all()
	success_url   = reverse_lazy('pais:list')
	template_name = 'pais_delete.html'

	def get_context_data(self, **kwarg):
		context = super(PaisDeleteView, self).get_context_data(**kwarg)
		is_auth = False 
		name    = None
		if self.request.user.is_authenticated():
			is_auth = True
			name    = self.request.user.username

		data = {
			'is_auth':is_auth,
			'name'   :name
		}

		context.update(data)
		return context


class PaisDetailView(DetailView):
	model = Pais 
	template_name = 'pais_detail.html'

	def get_context_data(self, **kwarg):
		context = super(PaisDetailView, self).get_context_data(**kwarg)
		is_auth = False 
		name    = None
		if self.request.user.is_authenticated():
			is_auth = True
			name    = self.request.user.username

		data = {
			'is_auth':is_auth,
			'name'   :name
		}

		context.update(data)
		return context

		
class PaisListView(ListView):
	model         = Pais 
	template_name = 'pais_list.html'
	paginate_by   = 10
	def get_context_data(self, **kwarg):
		context = super(PaisListView, self).get_context_data(**kwarg)
		is_auth = False 
		name    = None
		if self.request.user.is_authenticated():
			is_auth = True
			name    = self.request.user.username

		data = {
			'is_auth':is_auth,
			'name'   :name
		}

		context.update(data)
		return context


class PaisViewSet(viewsets.ModelViewSet):
	model      		 = Pais 
	serializer_class = PaisSerializer
	queryset         = Pais.objects.all()