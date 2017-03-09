from django.forms import ModelForm
from django import forms

from Costumer.models import*

class Data_Pelanggan_Form(ModelForm):
    class Meta:
        model = Data_Pelanggan
        fields = ['nama_pelanggan', 'alamat_pelanggan', 'nomer_telepon']
        labels = {

            'nama_pelanggan': 'Nama Pelanggan',
            'alamat_pelanggan': 'Alamat',
            'nomer_telepon': 'Nomer Telepon'
        }

        error_messages = {

            'nama_pelanggan': {
                'required': 'Anda harus mengisi nama'
            },
            'alamat_pelanggan': {
                'required': 'Anda harus mengisi alamat'
            },
            'nomer_telepon': {
                'required': 'Anda haru mengisi nomer telepon'
            }

        }

        widget = {
            'alamat_pelanggan': forms.Textarea(attrs={'col': 60, 'row': 10})
        }

class Data_Pemesanan_Form(ModelForm):
    class Meta:
        model = Data_Pemesanan
        fields = ['kode_pelanggan']
        labels = {

            'kode_pelanggan': 'Pelanggan',
        }

        error_messages = {

            'kode_pelanggan': {
                'required': 'Anda harus memilih Pelanggan'
            }
        }


class DetailPemesanan_Form(ModelForm):
    class Meta:
        model = DetailPemesanan
        fields = ['kode_pemesanan', 'kode_obat', 'kode_resep', 'jumlah']
        labels = {

            'kode_pemesanan': 'Pemesan',
            'kode_obat': 'Obat',
            'kode_resep': 'Resep',
            'jumlah': 'Jumlah'
        }

        error_messages = {

            'kode_pemesanan': {
                'required': 'Anda harus memilih Pemesan'
            },
            'kode_obat': {
                'required': 'Anda harus memilih obat'
            },
            'kode_resep': {
                'required': 'Anda harus memilih resep'
            },
            'jumlah': {
                'required': 'Anda harus mengisi jumlah'
            }
        }
