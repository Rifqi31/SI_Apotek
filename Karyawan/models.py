from __future__ import unicode_literals

from django.db import models
from django.conf import
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator

# Create your models here.

class Karyawan(models.Model):

    kode_karyawan = models.CharField(
        primary_key = True,
        max_length = 5,
        validators=[RegexValidator(r'^\d{1,10}$')])
    )

    nama_karyawan = models.CharField(max_length = 50)
    tanggal_lahir_karyawan = models.DateField()
    alamat_karyawawn = models.TextField(validators=[MaxLengthValidator(100)])
    telepon_karyawan = models.CharField(max_length = 20, validators=[RegexValidator(r'^\d{1,10}$')])
    email_karyawan = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.kode_karyawan
