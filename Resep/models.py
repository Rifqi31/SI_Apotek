from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

# Create your models here.

class Resep(models.Model):

    kode_resep = models.CharField(
        primary_key = True,
        max_length = 5,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )

    tanggal_resep = models.DateField()
    nama_pasien = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.kode_resep
