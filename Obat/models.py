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
        return self.nama_obat


class Data_Obat(models.Model):
    jenis_obat = {

        ('obat bebas', 'Obat Bebas'),
        ('obat bebas terbatas', 'Obat Bebas Terbatas'),
        ('obat keras', 'Obat Keras')
    }

    bentuk_obat = {

        ('serbuk', 'Serbuk'),
        ('tablet', 'Tablet'),
        ('pil', 'PIL'),
        ('kapsul', 'Kapsul'),
        ('larutan', 'Larutan'),
        ('suspensi', 'Suspensi'),
        ('salep', 'Salep')

    }

    kode_obat = models.CharField(
        primary_key=True,
        max_length=5,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )
    nama_obat = models.ForeignKey(Data_Pembelian, null=True)
    jenis_obat = models.CharField(choices=jenis_obat, max_length=20)
    bentuk_obat = models.CharField(max_length=20, choices=bentuk_obat)
    harga_obat = MoneyField(max_digits=10, decimal_places=2, default_currency='IDR')
    stock_obat = models.IntegerField()
    nama_suplier = models.ForeignKey(Data_Suplier)
    
    def __unicode__(self):
        return self.nama_obat.nama_obat



class Data_Resep(models.Model):
    kode_resep = models.CharField(
        primary_key=True,
        max_length=5,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )

    tanggal_resep = models.DateField()
    nama_pasien = models.CharField(max_length=50)

    def __unicode__(self):
        return self.kode_resep
