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
from django.views.generic import TemplateView
from django.views.generic import View


from .models import Usuario
from .forms import UsuarioForm, UserCreationEmailForm

from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets

import socket


class Login(FormView):
    form_class = AuthenticationForm
    template_name = 'usuario_login_form.html'
    success_url   =  reverse_lazy('usuario:template')

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


class UsuarioTemplateView(TemplateView):
	template_name = 'usuario_template.html'

	def get_context_data(self, **kwargs):
		context = super(UsuarioTemplateView, self).get_context_data(**kwargs)	
		is_auth  = False 
		username = None
		avatar   = None

		if self.request.user.is_authenticated():
			id_usuario  = self.get_user_id()
			is_auth 	= True
			username    = self.get_username()
			avatar 		= self.get_user_avatar()

		data = {
			'id_usuario' : id_usuario,
			'is_auth'	 : is_auth,
			'username'   : username,
			'avatar'	 : avatar,
		}

		context.update(data)
		return context

	def get_user_id(self):
		return self.request.user.id 

	def get_username(self):
		return self.request.user.username

	def get_user_avatar(self):
		return self.request.user.avatar


class UsuarioCreateView(CreateView):
	form_class    = UserCreationEmailForm
	models        = Usuario
	success_url   =  '/admin/'
	template_name = 'usuario_create.html'

	def form_valid(self, form):

	    self.object 					  = form.save(commit=False)
	    #self.object.usuario_creador 	  = self.request.user
	    #self.object.ultimo_usuario_editor = self.object.usuario_creador
	    self.object.slug 				  = self.object.username
	    try:
	    	self.object.nombre_host = socket.gethostname()
	    except:
	       self.object.nombre_host  = 'localhost'

	    self.object.direccion_ip 	= socket.gethostbyname(socket.gethostname())
	    self.object.save()
	   
	    return super(UsuarioCreateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(UsuarioCreateView, self).get_context_data(**kwargs)
		is_auth  = False 
		username = None
		avatar   = None

		if self.request.user.is_authenticated():
			id_usuario  = self.get_user_id()
			is_auth 	= True
			username    = self.get_username()
			avatar 		= self.get_user_avatar()

		data = {
			'id_usuario' : id_usuario,
			'is_auth'	 : is_auth,
			'username'   : username,
			'avatar'	 : avatar,
		}

		context.update(data)
		return context

	def get_user_id(self):
		return self.request.user.id 

	def get_username(self):
		return self.request.user.username

	def get_user_avatar(self):
		return self.request.user.avatar

class UsuarioUpdateView(UpdateView):
	form_class  	= UsuarioForm
	models      	= Usuario
	success_url 	= reverse_lazy('usuario:list')
	template_name 	= 'usuario_update.html'
	queryset 		= Usuario.objects.all()

	def get_context_data(self, **kwarg):
		context  = super(UsuarioUpdateView, self).get_context_data(**kwarg)
		is_auth  = False
		username = None

		if self.request.user.is_authenticated():
			is_auth  = True
			username = self.request.user.username

		data = {
			'is_auth' : is_auth,
			'username': username,
		}

		context.update(data)
		return context


class UsuarioDetailView(DetailView):
	model = Usuario 
	template_name = 'usuario_detail.html'

	def get_context_data(self, **kwarg):
		context  = super(UsuarioDetailView, self).get_context_data(**kwarg)
		is_auth  = False 
		username = None
		if self.request.user.is_authenticated():
			is_auth = True
			username = self.request.user.username

		data = {
			'is_auth':is_auth,
			'username'   :username
		}

		context.update(data)
		return context

				
class UsuarioListView(ListView):
	model         = Usuario 
	template_name = 'usuario_list.html'
	paginate_by   = 10

	def get_context_data(self, **kwarg):
		context 	= super(UsuarioListView, self).get_context_data(**kwarg)
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