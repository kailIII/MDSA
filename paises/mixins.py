from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

from braces.views import LoginRequiredMixin
from braces.views import StaffuserRequiredMixin
from braces.views import SuperuserRequiredMixin
from braces.views import MultiplePermissionsRequiredMixin
from braces.views import AnonymousRequiredMixin


class BaseAccessRequiredMixin(object):
	
	@method_decorator(login_required(login_url='/admin/'))
	@method_decorator(permission_required('pais.add_departamento', login_url='/admin/'))
	@method_decorator(permission_required('pais.change_departamento', login_url='/admin/'))
	@method_decorator(permission_required('pais.delete_departamento', login_url='/admin/'))
	def dispatch(self, request, *args, **kwargs):
		return super(BaseAccessRequiredMixin, self).dispatch(request, *args, **kwargs)


class AccessUserRequiredMixin(LoginRequiredMixin, 
							  StaffuserRequiredMixin, 
							  MultiplePermissionsRequiredMixin, 
							  ):
	#LoginRequiredMixin
	login_url	  = '/admin/'
	#MultiplePermissionsRequiredMixin
	permissions   = {
		'all':( 'paises.add_pais', 
				'paises.change_pais', 
				'paises.delete_pais'),
	}

