# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Provincia
from .forms import ProvinciaForm
from .serializers import ProvinciaSerializer
from rest_framework import viewsets

# Create your views here.
class ProvinciaCreateView(CreateView):
	form_class    = ProvinciaForm
	models        = Provincia
	success_url   = '/admin/'
	template_name = 'provincia_create.html'

	def get_context_data(self, **kwarg):
		context = super(ProvinciaCreateView, self).get_context_data(**kwarg)
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


class ProvinciaDetailView(DetailView):
	model = Provincia 
	template_name = 'provincia_detail.html'

	def get_context_data(self, **kwarg):
		context = super(ProvinciaDetailView, self).get_context_data(**kwarg)
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

		
class ProvinciaListView(ListView):
	model         = Provincia 
	template_name = 'provincia_list.html'
	paginate_by   = 10
	def get_context_data(self, **kwarg):
		context = super(ProvinciaListView, self).get_context_data(**kwarg)
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


class ProvinciaViewSet(viewsets.ModelViewSet):
	model      		 = Provincia 
	serializer_class = ProvinciaSerializer
	queryset         = Provincia.objects.all()