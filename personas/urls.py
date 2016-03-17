# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [

	url(r'^create/$', views.PersonaCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[\d]+)$', views.PersonaUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>[\d]+)/$', views.PersonaDeleteView.as_view(), name='delete'),
    url(r'^detail/(?P<pk>[\d]+)/$', views.PersonaDetailView.as_view(), name='detail'),
    
    url(r'^list/$', views.PersonaListView.as_view(), name='list'),
    url(r'^$', views.PersonaTemplateView.as_view(), name='template'),
]