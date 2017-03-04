from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

from Pelanggan.models import Data_Pelanggan


# Create your models here.

class Data_Resep(models.Model):
    kode_resep = models.CharField(
        primary_key=True,
        max_length=5,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )

    tanggal_resep = models.DateField()
    kode_pelanggan = models.ForeignKey(Data_Pelanggan)
    nama_pasien = models.CharField(max_length=50)

    def __unicode__(self):
        return self.kode_resep
