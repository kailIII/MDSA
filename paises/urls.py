# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views
from rest_framework import routers  

router = routers.DefaultRouter()
router.register(r'paises', views.PaisViewSet.as_view())

urlpatterns = [
    url(r'^create/$', views.PaisCreateView.as_view(), name='create'),
    url(r'^api/', include(router.urls, namespace="api_rest")),
]