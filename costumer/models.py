from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.utils import timezone

from obat.models import obat

# Create your models here.

class costumer(models.Model):

	kd_costumer = models.CharField(primary_key = True, default = '', max_length = 10, validators=[RegexValidator(r'^\d{1,10}$')], unique = True)
	nama_costumer = models.CharField(max_length = 15)
	alamat_costumer = models.TextField(validators=[MaxLengthValidator(100)])
 	
	def __unicode__(self):
		return self.kd_costumer


class penjualan_obat(models.Model):

	kd_penjualan = models.CharField(primary_key = True, default = '', max_length = 10, validators=[RegexValidator(r'^\d{1,10}$')], unique = True)
	kd_costumer_obat = models.ForeignKey(costumer)
	tgl_penjualan = models.DateField(auto_now_add = True)
	total_penjualan = models.IntegerField()

	def __unicode__(self):
		return self.kd_penjualan


class detail_penjualan_obat(models.Model):

	kd_penjualan_detail = models.ForeignKey(penjualan_obat)
	kd_obat_detail = models.ForeignKey(obat)
	jumlah_jual = models.IntegerField()
	total_harga_perobat = models.IntegerField()

	def __unicode__(self):
		return self.total_harga_perobat
