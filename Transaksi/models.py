from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

# django money field
from djmoney.models.fields import MoneyField

from Costumer.models import Data_Pelanggan

# Create your models here.

class Data_Penjualan(models.Model):
    kode_penjualan = models.CharField(
        primary_key=True,
        max_length=5,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )

    nama_pelanggan = models.ForeignKey(Data_Pelanggan)
    total_barang = models.IntegerField()
    total_penjualan = MoneyField(max_digits=10, decimal_places=2, default_currency='IDR')

    def __unicode__(self):
        return self.nama_pelanggan
