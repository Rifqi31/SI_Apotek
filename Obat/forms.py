from django.forms import ModelForm

from Obat.models import Data_Obat


class Data_Obat_Form(ModelForm):
    class Meta:
        model = Data_Obat
        fields = ['kode_pembelian_suplier', 'jenis_obat', 'bentuk_obat', 'harga_obat', 'kode_suplier']
        labels = {

            'kode_pembelian_suplier': 'Kode Pembelian Suplier',
            'jenis_obat': 'Jenis Obat',
            'bentuk_obat': 'Bentuk Obat',
            'harga_obat': 'Harga Obat',
            'kode_suplier': 'Suplier',
        }

        error_messages = {

            'kode_pembelian_suplier': {
                'required': 'Anda harus memilih kode pembelian dari suplier'
            },

            'jenis_obat': {
                'required': 'Anda harus memilih jenis obat'
            },
            'bentuk_obat': {
                'required': 'Anda harus memilih bentuk obat'
            },
            'harga_obat': {
                'required': 'Anda harus mengisi harga obat'
            },

            'stock_obat': {
                'required': 'Anda harus mengisi stock obat'
            },
            'kode_suplier': {
                'required': 'Anda harus memilih suplier'
            }
        }
