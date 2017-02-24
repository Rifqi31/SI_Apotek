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


class DetailPemesanan_Form(ModelForm):

    class Meta:

        model = DetailPemesanan
        fields = ['kode_pemesanan','kode_obat','kode_resep','jumlah']
        labels = {

            'kode_pemesanan':'Kode Pemesanan',
            'kode_obat':'Kode Obat',
            'kode_resep':'Kode Resep',
            'jumlah':'Jumlah'
        }

        error_messages = {

            'kode_pemesanan':{
                'required':'Anda harus memilih kode Pemesanan'
            },
            'kode_obat':{
                'required':'Anda harus memilih kode obat'
            },
            'kode_resep':{
                'required':'Anda harus memilih kode resep'
            },
            'jumlah':{
                'required':'Anda harus mengisi jumlah'
            }
        }
