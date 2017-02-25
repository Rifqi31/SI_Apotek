from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
import datetime

#import models
from Pemesanan.models import Pemesanan
from Obat.models import Obat

# Create your models here.

class Penjualan(models.Model):

    kode_penjualan = models.CharField(
        primary_key = True,
        max_length = 5,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )

    kode_pemesanan = models.ForeignKey(Pemesanan)
    tanggal_penjualan = models.DateField(auto_now_add = True)
    total_penjualan = models.MoneyField(max_digits=10, decimal_places=2, default_currency='IDR')

    def __unicode__(self):
        return self.kode_penjualan



class DetailPenjualan(models.Model):

	kode_penjualan = models.ForeignKey(Penjualan)
	kd_obat = models.ForeignKey(Obat)
	jumlah = models.IntegerField()
	total_harga_perobat = models.MoneyField(max_digits=10, decimal_places=2, default_currency='IDR')

	def __unicode__(self):
		return self.kode_penjualan