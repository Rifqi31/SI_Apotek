from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator

# Create your models here.

class Data_Pelanggan(models.Model):

	kode_pelanggan =  models.CharField(
		primary_key = True,
		max_length = 5,
		validators=[RegexValidator(r'^\d{1,10}$')]
	)
	nama_pelanggan = models.CharField(max_length = 50)
	alamat_pelanggan = models.TextField(validators=[MaxLengthValidator(100)])
	nomer_telepon = models.CharField(max_length = 20, validators=[RegexValidator(r'^\d{1,12}$')])
	
	def __unicode__(self):
		return self.kode_pelanggan