from django.forms import ModelForm

from Transaksi.models import*


class Data_Penjualan_Form(ModelForm):
    class Meta:
        model = Data_Penjualan
        fields = []
        labels = {}
        