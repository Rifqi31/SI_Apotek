from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class costumer(models.Model):

	kd_costumer = models.IntegerField(primary_key = True, default = '')
	nama_costumer = models.CharField(max_length = 15)
	alamat_costumer = models.TextField()

	def __unicode__(self):
		return self.kd_costumer