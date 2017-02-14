from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

# Create your models here.

class obat(models.Model):

	kd_obat = models.CharField(primary_key = True, default = '', max_length = 10, validators=[RegexValidator(r'^\d{1,10}$')])
	nama_obat = models.CharField(max_length = 15)
	tipe_obat = models.CharField(max_length = 15)
	harga_jual = models.IntegerField()

	def __unicode__(self):
		return self.kd_obat