from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
	
	list_display = ('username', 'email', 'password', 'avatar', 'slug', 'last_login', 'nombre_host', 'direccion_ip', 'is_staff', 'is_active')
	

	fieldsets = (
			('Usuario', {'fields':('username', 'password', 'email', 'avatar')}),

			('Permissions', {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')})
		)

	search_fields  = ('username',)

	class Meta:
		model = Usuario
		exclude = ('username')
		
# Register your models here.

#admin.site.register(Usuario, UsuarioAdmin)