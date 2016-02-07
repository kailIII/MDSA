# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Pais


class PaisSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model  = Pais
		fields = '__all__'