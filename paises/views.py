from django.shortcuts import render
from django.views.generic import CreateView

from .forms import PaisForm
from .models import Pais

from rest_framework import viewsets

# Create your views here.
class PaisCreateView(CreateView):
	form_class    = PaisForm
	models        = Pais
	success_url   = '/admin/'
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

class PaisViewSet(viewsets.ModelViewSet):
	model = Pais
	