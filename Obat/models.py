from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

#django money field
from djmoney.models.fields import MoneyField

# Create your models here.

class Obat(models.Model):

	jenis_obat = {

		('obat bebas','Obat Bebas'),
		('obat bebas terbatas','Obat Bebas Terbatas'),
		('obat keras','Obat Keras')
	}

	bentuk_obat = {

		('serbuk','Serbuk'),
		('tablet','Tablet'),
		('pil','PIL'),
		('kapsul','Kapsul'),
		('larutan','Larutan'),
		('suspensi','Suspensi'),
		('salep','Salep')

	}

	kode_obat =  models.CharField(
		primary_key = True,
		max_length = 5,
		validators=[RegexValidator(r'^\d{1,10}$')]
	)

	nama_obat = models.CharField(max_length = 100)
	jenis_obat = models.CharField(max_length = 20, choices = jenis_obat)
	bentuk_obat = models.CharField(max_length = 20, choices = bentuk_obat)
	harga_obat = MoneyField(max_digits=10, decimal_places=2, default_currency='IDR')
	stock_obat = models.IntegerField()

	def __unicode__(self):
		return self.kode_obat