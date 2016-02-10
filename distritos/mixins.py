from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):

	@method_decorator(login_required(login_url='/admin/'))
	@method_decorator(permission_required('distritos.add_distrito', login_url='/admin/'))
	@method_decorator(permission_required('distritos.change_distrito', login_url='/admin/'))
	@method_decorator(permission_required('distritos.delete_distrito', login_url='/admin/'))
	def dispatch(self, request, *arg, **kwarg):
		return super(LoginRequiredMixin, self).dispatch(request, *arg, **kwarg)