from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
import datetime

#import models
from Pelanggan.models import*
from Karyawan.models import BiodataKaryawan

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
