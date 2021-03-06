from django.forms import ModelForm

from Pembelian.models import Data_Pembelian


class Data_Pembelian_Form(ModelForm):
    class Meta:
        model = Data_Pembelian
        fields = ['kode_suplier', 'nama_obat', 'harga_beli', 'total_barang']
        labels = {

            'kode_suplier': 'Kode Suplier',
            'nama_obat': 'Nama Produk Obat',
            'harga_beli': 'Harga Beli',
            'total_barang': 'Total Barang'
        }
