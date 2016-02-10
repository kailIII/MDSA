# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.ProvinciaCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[\w\-]+)/$', views.ProvinciaUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>[\w\-]+)/$', views.ProvinciaDeleteView.as_view(), name='delete'),
    url(r'^detail/(?P<pk>[\w\-]+)/$', views.ProvinciaDetailView.as_view(), name='detail'),
    url(r'^list/', views.ProvinciaListView.as_view(), name='list'),
]
