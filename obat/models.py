from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class obat(models.Model):

	kd_obat = models.IntegerField(primary_key = True)
	nama_obat = models.CharField(max_length = 15)
	tipe_obat = models.CharField(max_length = 15)
	harga_jual = models.IntegerField()

	def __unicode__(self):
		return self.kd_obat