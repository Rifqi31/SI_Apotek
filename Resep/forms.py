from django.forms import ModelForm

from Resep.models import Data_Resep


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
