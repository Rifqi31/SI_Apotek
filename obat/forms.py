from django.forms import ModelForm
from django import forms

from obat.models import obat

class obat_form(ModelForm):
	class Meta:

		model = obat
		fields = ['nama_obat','tipe_obat','harga_jual']
		labels = {

			'nama_obat' : 'Nama',
			'tipe_obat' : 'Tipe obat',
			'harga_jual' : 'Harga',
		}

		error_messages = {

			'nama_obat':{
				'required':'Anda harus mengisi nama obat'
			},

			'tipe_obat':{
				'required':'Anda harus mengisi tipe obat'
			},

			'harga_jual':{
				'required':'Anda harus mengisi harga'
			}
		}