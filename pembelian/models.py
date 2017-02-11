from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from django.utils import timezone

from suplier.models import suplier
from obat.models import obat

# Create your models here.

class pembelian_obat(models.Model):

	kd_pembelian = models.IntegerField(primary_key = True)
	kd_suplier_obat = models.ForeignKey(suplier)
	tgl_pembelian = models.DateField()
	total_pembelian = models.IntegerField()


	def __unicode__(self):
		return self.kd_suplier_obat.kd_suplier


class detail_pembelian(models.Model):

	kd_pembelian_detail = models.ForeignKey(pembelian_obat)
	kd_obat_detail = models.ForeignKey(obat)
	jumlah_beli = models.IntegerField()
	total_harga_perobat = models.IntegerField()

	def __unicode__(self):
		return (self.kd_pembelian_detail.kd_pembelian, self.kd_obat_detail.kd_obat)
