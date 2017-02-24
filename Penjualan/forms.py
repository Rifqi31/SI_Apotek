from django.forms import ModelForm
from django import forms

from Penjualan.models import*

class Penjualan_Form(ModelForm):

    class Meta:

        model = Penjualan
        fields = ['kode_pemesanan']
        labels = {

            'kode_pemesanan':'Kode Pemesanan',
        }

        error_messages = {

            'kode_pemesanan':{
                'required':'Anda harus memilih kode Pelanggan'
            }
        }
