from django.forms import ModelForm

from Obat.models import Data_Obat, Data_Resep, Data_Pembelian


class Data_Pembelian_Form(ModelForm):
    class Meta:
        model = Data_Pembelian
        fields = ['kode_suplier', 'nama_obat', 'harga_beli', 'total_barang']
        labels = {

            'kode_suplier': 'Suplier',
            'nama_obat': 'Nama Produk Obat',
            'harga_beli': 'Harga Beli',
            'total_barang': 'Total Barang'
        }


class Data_Obat_Form(ModelForm):
    class Meta:
        model = Data_Obat
        fields = ['nama_obat', 'jenis_obat', 'bentuk_obat', 'harga_obat', 'nama_suplier']
        labels = {

            'nama_obat': 'Nama Obat',
            'jenis_obat': 'Jenis Obat',
            'bentuk_obat': 'Bentuk Obat',
            'harga_obat': 'Harga Obat',
            'nama_suplier': 'Suplier',
        }

        error_messages = {

            'nama_obat': {
                'required': 'Anda harus memilih nama obat'
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
            'nama_suplier': {
                'required': 'Anda harus memilih suplier'
            }
        }



class Resep_Form(ModelForm):
    class Meta:
        model = Data_Resep
        fields = ['tanggal_resep', 'nama_pasien']
        labels = {

            'tanggal_resep': 'Tanggal',
            'nama_pasien': 'Nama Pasien',
        }

        error_messages = {

            'tanggal_resep': {
                'required': 'Anda harus mengisi tanggal'
            },
            'nama_pasien': {
                'required': 'Anda harus mengisi nama pasien'

            }
        }
