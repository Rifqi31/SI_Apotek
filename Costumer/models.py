from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
# django money field
from djmoney.models.fields import MoneyField

from Karyawan.models import Biodata_karyawan
from Obat.models import Data_Obat
from Resep.models import Data_Resep

# Create your models here.
class Data_Pelanggan(models.Model):
    kode_pelanggan = models.CharField(
        primary_key=True,
        max_length=5,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )
    nama_pelanggan = models.CharField(max_length=50)
    alamat_pelanggan = models.TextField(validators=[MaxLengthValidator(100)])
    nomer_telepon = models.CharField(max_length=20, validators=[RegexValidator(r'^\d{1,12}$')])

    def __unicode__(self):
        return self.kode_pelanggan


class Data_Pemesanan(models.Model):
    kode_pemesanan = models.CharField(
        primary_key=True,
        max_length=5,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )

    tanggal_pemesanan = models.DateField(auto_now_add=True)
    kode_pelanggan = models.ForeignKey(Data_Pelanggan)
    nama_pelanggan = models.CharField(max_length=50)
    karyawan = models.ForeignKey(Biodata_karyawan)

    def __unicode__(self):
        return self.kode_pemesanan


class DetailPemesanan(models.Model):
    kode_pemesanan = models.ForeignKey(Data_Pemesanan)
    nama_pemesan = models.CharField(max_length=50)
    kode_obat = models.ForeignKey(Data_Obat)
    nama_obat = models.CharField(max_length=50)
    kode_resep = models.ForeignKey(Data_Resep, blank=True)
    jumlah = models.IntegerField()
    total_harga_perobat = MoneyField(max_digits=10, decimal_places=2, default_currency='IDR')

    def __unicode__(self):
        return self.kode_pemesanan.kode_pemesanan
