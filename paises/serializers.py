# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from .models import Pais

class PaisSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Pais
		fields = '__all__'