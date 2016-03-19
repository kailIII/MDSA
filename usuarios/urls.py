# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^login/$', views.Login.as_view(), name='login'),
	url(r'^logout/$', views.Logout.as_view(), name='login'),

	url(r'^create/$', views.UsuarioCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.UsuarioUpdateView.as_view(), name='update'),
    #url(r'^delete/(?P<pk>\d+)/$', views.UsuarioDeleteView.as_view(), name='delete'),
    url(r'^detail/(?P<pk>\d+)/$', views.UsuarioDetailView.as_view(), name='detail'),
    url(r'^list/$', views.UsuarioListView.as_view(), name='list'),
    url(r'^$', views.UsuarioTemplateView.as_view(), name='template'),
]