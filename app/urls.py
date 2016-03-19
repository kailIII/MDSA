"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static

from rest_framework import routers

#ViewSet 
from paises.views import PaisViewSet 
from usuarios.views import UsuarioViewSet, GroupViewSet, PermissionViewSet

router = routers.DefaultRouter()
router.register(r'paises', PaisViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
 	url(r'^pais/', include('paises.urls', namespace='pais')),
 	url(r'^departamento/', include('departamentos.urls', namespace='departamento')),
 	url(r'^provincia/', include('provincias.urls', namespace='provincia')),
 	url(r'^distrito/', include('distritos.urls', namespace='distrito')),

 	url(r'^documento_identificacion/', include('documentos_identificaciones.urls', namespace='documento_identificacion')),
 	url(r'^estado_civil/', include('estados_civiles.urls', namespace='estado_civil')),

 	url(r'^usuario/', include('usuarios.urls', namespace='usuario')),
 	url(r'^persona/', include('personas.urls', namespace='persona')),
 	url(r'^api/', include(router.urls))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
