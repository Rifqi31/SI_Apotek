from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User


# Create your models here.
class Biodata_karyawan(models.Model):
    waktu_kerja = [

        ('pagi/siang', 'Pagi/Siang'),
        ('malam', 'Malam')
    ]
    nama_karyawan = models.CharField(max_length=50)
    tanggal_lahir = models.DateField()
    alamat = models.TextField(validators=[MaxLengthValidator(100)])
    telepon = models.CharField(max_length=20, validators=[RegexValidator(r'^\d{1,12}$')])
    email_karyawan = models.EmailField(blank=True)
    shift_kerja = models.CharField(max_length=10, choices=waktu_kerja)

    @property
    def __unicode__(self):
        return self.nama_karyawan


class Akun_karyawan(models.Model):
    akun = models.ForeignKey(User)
    karyawan = models.ForeignKey(Biodata_karyawan)

    @property
    def __unicode__(self):
        return self.karyawan.nama_karyawan


class Absen_karyawan(models.Model):
    jenis_absen = {

        (u'hadir', u'Hadir'),
        (u'izin', u'Izin'),
        (u'cuti', u'Cuti'),
        (u'alpa', u'Tanpa Kehadiran'),

    }

    karyawan = models.ForeignKey(Akun_karyawan)
    jenis_kehadiran = models.CharField(max_length=50, choices=jenis_absen, default='hadir')
    waktu = models.DateField(auto_now_add=True)

    @property
    def __unicode__(self):
        return self.karyawan.akun


class Izin_karyawan(models.Model):
    jenis_izin = {

        ('izin', 'Izin'),
        ('cuti', 'Cuti'),
    }

    karyawan = models.ForeignKey(Biodata_karyawan)
    jenis_kehadiran = models.CharField(max_length=50, choices=jenis_izin)
    waktu_mulai = models.DateField(auto_now_add=True)
    waktu_berhenti = models.DateField()
    alasan = models.TextField(validators=[MaxLengthValidator(150)])
    disetujui = models.BooleanField(default=False)

    @property
    def __unicode__(self):
        return self.karyawan.nama_karyawan
