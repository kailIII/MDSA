# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.DepartamentoCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[\w\-]+)/$', views.DepartamentoUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>[\w\-]+)/$', views.DepartamentoDeleteView.as_view(), name='delete'),
    url(r'^detail/(?P<pk>[\w\-]+)/$', views.DepartamentoDetailView.as_view(), name='detail'),
    url(r'^list/', views.DepartamentoListView.as_view(), name='list'),
]
