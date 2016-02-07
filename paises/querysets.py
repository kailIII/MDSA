# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PaisQuerySet(QuerySet):

	def top(self):
		return self.order_by('-id')[:10]