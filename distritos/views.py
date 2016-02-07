# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Distrito
from .forms import DistritoForm
from .serializers import DistritoSerializer
from rest_framework import viewsets

# Create your views here.
class DistritoCreateView(CreateView):
	form_class    = DistritoForm
	models        = Distrito
	success_url   = '/admin/'
	template_name = 'distrito_create.html'

	def get_context_data(self, **kwarg):
		context = super(DistritoCreateView, self).get_context_data(**kwarg)
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


class DistritoDetailView(DetailView):
	model = Distrito 
	template_name = 'distrito_detail.html'

	def get_context_data(self, **kwarg):
		context = super(DistritoDetailView, self).get_context_data(**kwarg)
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

		
class DistritoListView(ListView):
	model         = Distrito 
	template_name = 'distrito_list.html'
	paginate_by   = 10
	def get_context_data(self, **kwarg):
		context = super(DistritoListView, self).get_context_data(**kwarg)
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


class DistritoViewSet(viewsets.ModelViewSet):
	model      		 = Distrito 
	serializer_class = DistritoSerializer
	queryset         = Distrito.objects.all()