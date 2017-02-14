from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

from obat.models import obat

# Create your models here.
class suplier(models.Model):

	kd_suplier = models.CharField(primary_key = True, default = '', max_length = 10, validators=[RegexValidator(r'^\d{1,10}$')])
	nama_suplier = models.CharField(max_length = 15)
	alamat_suplier = models.TextField()

	def __unicode__(self):
		return self.kd_suplier


class pembelian_obat(models.Model):

	kd_pembelian = models.CharField(primary_key = True, default = '', max_length = 10, validators=[RegexValidator(r'^\d{1,10}$')])
	kd_suplier_obat = models.ForeignKey(suplier)
	tgl_pembelian = models.DateField()
	total_pembelian = models.IntegerField()

	def __unicode__(self):
		return self.kd_suplier_obat.kd_suplier


class detail_pembelian_obat(models.Model):

	kd_pembelian_detail = models.ForeignKey(pembelian_obat)
	kd_obat_detail = models.ForeignKey(obat)
	jumlah_beli = models.IntegerField()
	total_harga_perobat = models.IntegerField()

	def __unicode__(self):
		return self.total_harga_perobat
