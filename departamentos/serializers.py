# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from .models import Departamento


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model  = Departamento
		fields = '__all__'