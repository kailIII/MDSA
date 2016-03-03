# -*- encoding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters

from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import FormView
from django.views.generic import View

from .models import Usuario
from .forms import UsuarioForm, UserCreationEmailForm

from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets

import socket


class Login(FormView):
    form_class = AuthenticationForm
    template_name = 'login_usuario_form.html'
    success_url   =  '/admin/'

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        return super(Login, self).form_invalid(form)

    @method_decorator(sensitive_post_parameters('password'))
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(Login, self).dispatch(request, *args, **kwargs)


class Logout(View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super().get(self, request, *args, **kwargs)


class UsuarioCreateView(CreateView):
	form_class    = UserCreationEmailForm
	models        = Usuario
	success_url   =  '/admin/'
	template_name = 'usuario_create.html'

	def form_valid(self, form):

	    self.object 					  = form.save(commit=False)
	    self.object.usuario_creador 	  = self.request.user
	    self.object.ultimo_usuario_editor = self.object.usuario_creador
	    self.object.slug 				  = self.object.username
	    try:
	    	self.object.nombre_host = socket.gethostname()
	    except:
	       self.object.nombre_host  = 'localhost'

	    self.object.direccion_ip 	= socket.gethostbyname(socket.gethostname())
	    self.object.save()

	    return super(UsuarioCreateView, self).form_valid(form)

	def get_context_data(self, **kwarg):
		context  = super(UsuarioCreateView, self).get_context_data(**kwarg)
		is_auth  = False 
		username = None
		if self.request.user.is_authenticated():
			is_auth 	= True
			username    = self.request.user.username

		data = {
			'is_auth'	 :is_auth,
			'username'   :username
		}

		context.update(data)
		return context