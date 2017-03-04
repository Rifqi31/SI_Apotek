from django.forms import ModelForm
from django import forms

from Resep.models import Data_Resep

class Resep_Form(ModelForm):

	class Meta:

		model = Data_Resep
		fields = ['tanggal_resep','kode_pelanggan']
		labels = {

			'tanggal_resep':'Tanggal',
			'Kode_pelanggan':'Kode Pelanggan',
		}

		error_messages = {

			'tanggal_resep':{
				'required':'Anda harus mengisi tanggal'
			},
			'kode_pelanggan':{
				'required':'Anda harus memilih kode pelanggan'

			}
		}