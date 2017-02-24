from django.forms import ModelForm
from django import forms

from Pemesanan.models import*

class Pemesanan_Form(ModelForm):

    class Meta:

        model = Pemesanan
        fields = ['kode_pelanggan','kode_karyawan']
        labels = {

            'kode_pelanggan':'Kode Pelanggan',
            'kode_karyawan':'Kode Karyawan'
        }

        error_messages = {

            'kode_pelanggan':{
                'required':'Anda harus memilih kode Pelanggan'
            },
            'kode_karyawan':{
                'required':'Anda harus memilih kode kode karyawan'
            }
        }
