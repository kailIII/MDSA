# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Distrito
from .mixins import LoginRequiredMixin 
from .forms import DistritoForm
from .serializers import DistritoSerializer

from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets

# Create your views here.
class DistritoCreateView(LoginRequiredMixin, CreateView):
	form_class    = DistritoForm
	models        = Distrito
	success_url   = reverse_lazy('distrito:list')
	template_name = 'distrito_create.html'

	def get_context_data(self, **kwarg):
		context  = super(DistritoCreateView, self).get_context_data(**kwarg)
		is_auth  = False 
		username = None
		if self.request.user.is_authenticated():
			is_auth  = True
			username = self.request.user.username

		data = {
			'is_auth'  :is_auth,
			'username' :username
		}

		context.update(data)
		return context


class DistritoUpdateView(LoginRequiredMixin, UpdateView):
	form_class    = DistritoForm
	models        = Distrito
	success_url   = reverse_lazy('distrito:list')
	template_name = 'distrito_update.html'

	def get_context_data(self, **kwarg):
		context  = super(DistritoUpdateView, self).get_context_data(**kwarg)
		is_auth  = False 
		username = None
		if self.request.user.is_authenticated():
			is_auth = True
			username    = self.request.user.username

		data = {
			'is_auth'  :is_auth,
			'username' :username
		}

		context.update(data)
		return context


class DistritoDeleteView(LoginRequiredMixin, DeleteView):
	models        = Distrito
	success_url   = reverse_lazy('distrito:list')
	template_name = 'distrito_delete.html'

	def get_context_data(self, **kwarg):
		context = super(DistritoDeleteView, self).get_context_data(**kwarg)
		is_auth = False 
		username    = None
		if self.request.user.is_authenticated():
			is_auth  = True
			username = self.request.user.username

		data = {
			'is_auth':is_auth,
			'username'   :username
		}

		context.update(data)
		return context


class DistritoDetailView(LoginRequiredMixin, DetailView):
	model = Distrito 
	template_name = 'distrito_detail.html'

	def get_context_data(self, **kwarg):
		context  = super(DistritoDetailView, self).get_context_data(**kwarg)
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

		
class DistritoListView(LoginRequiredMixin, ListView):
	model         = Distrito 
	template_name = 'distrito_list.html'
	paginate_by   = 10
	def get_context_data(self, **kwarg):
		context = super(DistritoListView, self).get_context_data(**kwarg)
		is_auth = False 
		username    = None
		if self.request.user.is_authenticated():
			is_auth  = True
			username = self.request.user.username

		data = {
			'is_auth' :is_auth,
			'username':username
		}

		context.update(data)
		return context


class DistritoViewSet(viewsets.ModelViewSet):
	model      		 = Distrito 
	serializer_class = DistritoSerializer
	queryset         = Distrito.objects.all()