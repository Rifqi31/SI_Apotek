from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
import datetime

#import models
from Pemesanan.models import Pemesanan

# Create your models here.

class Penjualan(models.Model):

    kode_penjualan = models.CharField(
        primary_key = True,
        max_length = 5,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )

    kode_pemesanan = models.ForeignKey(Pemesanan)
    tanggal_penjualan = models.DateField(auto_now_add = True)

    def __unicode__(self):
        return self.kode_penjualan