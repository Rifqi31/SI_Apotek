from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator


# Create your models here.

class Data_Suplier(models.Model):
    kode_suplier = models.CharField(
        primary_key=True,
        max_length=5,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )
    nama_suplier = models.CharField(max_length=50)
    alamat_suplier = models.TextField(validators=[MaxLengthValidator(100)])
    telepon_suplier = models.CharField(max_length=20, validators=[RegexValidator(r'^\d{1,12}$')])
    email_suplier = models.EmailField()

    def __unicode__(self):
        return self.nama_suplier
