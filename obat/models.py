from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

from djmoney.models.fields import MoneyField

# Create your models here.

class obat(models.Model):

	jenis_obat = {

		('obat bebas','Obat Bebas'),
		('obat bebas terbatas','Obat Bebas Terbatas'),
		('obat keras dan psikotropika','Obat Keras dan Psikotropika')
	}

	kd_obat = models.CharField(primary_key = True, default = '', max_length = 10, validators=[RegexValidator(r'^\d{1,10}$')])
	nama_obat = models.CharField(max_length = 15)
	tipe_obat = models.CharField(max_length = 35, choices = jenis_obat)
	harga_jual = MoneyField(max_digits=10, decimal_places=2, default_currency='IDR')

	def __unicode__(self):
		return self.kd_obat