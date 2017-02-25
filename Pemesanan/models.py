from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
import datetime

#import models
from Pelanggan.models import*
from Karyawan.models import BiodataKaryawan
from Obat.models import*
from Resep.models import*

# Create your models here.

class Pemesanan(models.Model):

    kode_pemesanan = models.CharField(
        primary_key = True,
        max_length = 5,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )

    tanggal_pemesanan = models.DateField(auto_now_add = True)
    kode_pelanggan = models.ForeignKey(Pelanggan)
    kode_karyawan = models.ForeignKey(BiodataKaryawan)

    def __unicode__(self):
        return self.kode_pemesanan



class DetailPemesanan(models.Model):

    kode_pemesanan = models.ForeignKey(Pemesanan)
    kode_obat = models.ForeignKey(Obat)
    kode_resep = models.ForeignKey(Resep)
    jumlah = models.IntegerField()
    total_harga_perobat = models.MoneyField(max_digits=10, decimal_places=2, default_currency='IDR')


    def __unicode__(self):
        return self.kode_pemesanan