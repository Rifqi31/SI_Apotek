from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class BiodataKaryawan(models.Model):

    nama_karyawan = models.CharField(max_length = 50)
    tanggal_lahir_karyawan = models.DateField()
    alamat_karyawan = models.TextField(validators=[MaxLengthValidator(100)])
    telepon_karyawan = models.CharField(max_length = 20, validators=[RegexValidator(r'^\d{1,12}$')])
    email_karyawan = models.EmailField(blank = True)

    def __unicode__(self):
        return self.nama_karyawan


#for create account karyawan
class Akun_karyawan(models.Model):

    waktu_kerja = {

        ('pagi/siang','Pagi/Siang'),
        ('malam','Malam')
    }

    akun = models.ForeignKey(User)
    karyawan = models.ForeignKey(BiodataKaryawan)
    shift_kerja = models.CharField(max_length = 10, choices = waktu_kerja)

    def __unicode__(self):
        return self.karyawan.nama_karyawan
