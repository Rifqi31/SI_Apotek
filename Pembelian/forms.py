from django.forms import ModelForm

from Pembelian.models import Data_Pembelian


class Data_Pembelian_Form(ModelForm):
    class Meta:
        model = Data_Pembelian
        fields = ['kode_suplier', 'total_barang']
        labels = {

            'kode_suplier': 'Kode Suplier',
            'total_barang': 'Total Barang'
        }
