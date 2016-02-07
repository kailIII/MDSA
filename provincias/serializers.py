# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from .models import Provincia


class ProvinciaSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model  = Provincia
		fields = '__all__'