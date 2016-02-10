from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):
	
	@method_decorator(login_required(login_url='/admin/'))
	@method_decorator(permission_required('pais.add_departamento', login_url='/admin/'))
	@method_decorator(permission_required('pais.change_departamento', login_url='/admin/'))
	@method_decorator(permission_required('pais.delete_departamento', login_url='/admin/'))
	def dispatch(self, request, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)