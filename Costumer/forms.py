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
        fields = ['pelanggan', 'nama_obat', 'kode_resep', 'jumlah']
        labels = {

            'pelanggan': 'Pelanggan',
            'nama_obat': 'Obat',
            'kode_resep': 'Resep',
            'jumlah': 'Jumlah'
        }

        error_messages = {

            'pelanggan': {
                'required': 'Anda harus memilih Pelanggan'
            },

            'nama_obat': {
                'required': 'Anda harus memilih obat'
            },
            'kode_resep': {
                'required': 'Anda harus memilih resep'
            },
            'jumlah': {
                'required': 'Anda harus mengisi jumlah'
            }
        }
