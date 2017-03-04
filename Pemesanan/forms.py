from django.forms import ModelForm
from django import forms

from Pemesanan.models import Data_Pemesanan, DetailPemesanan

class Data_Pemesanan_Form(ModelForm):

    class Meta:

        model = Data_Pemesanan
        fields = ['kode_pelanggan','karyawan']
        labels = {

            'kode_pelanggan':'Pelanggan',
            'kode_karyawan':'Karyawan'
        }

        error_messages = {

            'kode_pelanggan':{
                'required':'Anda harus memilih Pelanggan'
            },
            'karyawan':{
                'required':'Anda harus memilih karyawan'
            }
        }


class DetailPemesanan_Form(ModelForm):

    class Meta:

        model = DetailPemesanan
        fields = ['kode_pemesanan','kode_obat','kode_resep','jumlah']
        labels = {

            'kode_pemesanan':'Pemesan',
            'kode_obat':'Obat',
            'kode_resep':'Resep',
            'jumlah':'Jumlah'
        }

        error_messages = {

            'kode_pemesanan':{
                'required':'Anda harus memilih Pemesan'
            },
            'kode_obat':{
                'required':'Anda harus memilih obat'
            },
            'kode_resep':{
                'required':'Anda harus memilih resep'
            },
            'jumlah':{
                'required':'Anda harus mengisi jumlah'
            }
        }
