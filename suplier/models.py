from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class suplier(models.Model):

	kd_suplier = models.IntegerField(primary_key = True, default = '')
	nama_suplier = models.CharField(max_length = 15)
	alamat_suplier = models.TextField()

	def __unicode__(self):
		return self.kd_suplier