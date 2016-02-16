from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

from braces.views import LoginRequiredMixin
from braces.views import StaffuserRequiredMixin
from braces.views import SuperuserRequiredMixin
from braces.views import MultiplePermissionsRequiredMixin
from braces.views import AnonymousRequiredMixin


class BaseRequiredMixin(object):

	@method_decorator(login_required(login_url='/admin/'))
	@method_decorator(permission_required('provincias.add_provincia', login_url='/admin/'))
	@method_decorator(permission_required('provincias.change_provincia', login_url='/admin/'))
	@method_decorator(permission_required('provincias.delete_provincia', login_url='/admin/'))
	def dispatch(self, request, *arg, **kwarg):
		return super(LoginRequiredMixin, self).dispatch(request, *arg, **kwarg)


class AccessRequiredMixin(
							LoginRequiredMixin,
							StaffuserRequiredMixin,
							MultiplePermissionsRequiredMixin,
						 ):
	#LoginRequiredMixin
	login_url   = '/admin/'
	#MultiplePermissionsRequiredMixin
	permissions = {
		'all':(),

	}


