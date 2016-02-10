# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):
	
	@method_decorator(login_required(login_url='/admin/'))
	@method_decorator(permission_required('estados_civiles.add_estado_civil', login_url='/admin/'))
	@method_decorator(permission_required('estados_civiles.change_estado_civil', login_url='/admin/'))
	@method_decorator(permission_required('estados_civiles.delete_estado_civil', login_url='/admin/'))
	def dispatch(self, request, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)