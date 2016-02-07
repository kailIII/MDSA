# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.DistritoCreateView.as_view(), name='create'),
    url(r'^detail/(?P<pk>[\w\-]+)/$', views.DistritoDetailView.as_view(), name='detail'),
    url(r'^list/', views.DistritoListView.as_view(), name='list'),
]

