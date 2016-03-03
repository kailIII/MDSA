# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^login/$', views.Login.as_view(), name='login'),
	url(r'^logout/$', views.Logout.as_view(), name='login'),
    url(r'^create/$', views.UsuarioCreateView.as_view(), name='create'),
]