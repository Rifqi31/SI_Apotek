from django.forms import ModelForm

from Penjualan.models import Data_Penjualan


class Data_Penjualan_Form(ModelForm):
    class Meta:
        model = Data_Penjualan
        fields = []
        labels = {}