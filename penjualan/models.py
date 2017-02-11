from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from django.utils import timezone

from costumer.models import costumer
from obat.models import obat

# Create your models here.

class penjualan_obat(models.Model):

	kd_penjualan = models.IntegerField(primary_key = True)
	kd_costumer_obat = models.ForeignKey(costumer)
	tgl_penjualan = models.DateField()
	total_penjualan = models.IntegerField()

	def __unicode__(self):
		return self.kd_costumer_obat.kd_costumer


class detail_penjualan(models.Model):

	kd_penjualan_detail = models.ForeignKey(penjualan_obat)
	kd_obat_detail = models.ForeignKey(obat)
	jumlah_jual = models.IntegerField()
	total_harga_perobat = models.IntegerField()

	def __unicode__(self):
		return (self.kd_penjualan_detail.kd_penjualan, self.kd_obat_detail.kd_obat)