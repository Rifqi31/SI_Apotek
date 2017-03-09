from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

# django money field
from djmoney.models.fields import MoneyField

from Suplier.models import Data_Suplier

# Create your models here.
class Data_Pembelian(models.Model):
    kode_pembelian = models.CharField(
        primary_key=True,
        max_length=5,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )
    kode_suplier = models.ForeignKey(Data_Suplier, null=True)
    nama_suplier = models.CharField(max_length=50)
    nama_obat = models.CharField(max_length=50)
    tgl_pembelian = models.DateField(auto_now_add=True)
    harga_beli = MoneyField(max_digits=10, decimal_places=2, default_currency='IDR')
    total_barang = models.IntegerField()
    total_pembelian = MoneyField(max_digits=10, decimal_places=2, default_currency='IDR')

    def __unicode__(self):
        return self.kode_pembelian


class Data_Penjualan(models.Model):
    kode_penjualan = models.CharField(
        primary_key=True,
        max_length=5,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )

    nama_pelanggan = models.CharField(max_length=50)
    total_barang = models.IntegerField()
    total_penjualan = MoneyField(max_digits=10, decimal_places=2, default_currency='IDR')

    def __unicode__(self):
        return self.kode_penjualan

