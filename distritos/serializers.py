# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from .models import Distrito


class DistritoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Distrito
		fields = '__all__'