# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.PaisCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[\w\-]+)/$', views.PaisUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>[\w\-]+)/$', views.PaisDeleteView.as_view(), name='delete'),
    url(r'^detail/(?P<pk>[\w\-]+)/$', views.PaisDetailView.as_view(), name='detail'),
    url(r'^list/$', views.PaisListView.as_view(), name='list'),
]
