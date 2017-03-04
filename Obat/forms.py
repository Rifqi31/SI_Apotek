from django.forms import ModelForm
from django import forms

from Obat.models import Data_Obat

class Data_Obat_Form(ModelForm):

	class Meta:

		model = Data_Obat
		fields = ['nama_obat','jenis_obat','bentuk_obat','harga_obat','stock_obat','kode_suplier']
		labels = {

			'nama_obat' : 'Nama Obat',
			'jenis_obat' : 'Jenis Obat',
			'bentuk_obat' : 'Bentuk Obat',
			'harga_obat' : 'Harga Obat',
			'stock_obat' : 'Stock',
			'kode_suplier' : 'Suplier',
		}

		error_messages = {

			'nama_obat':{
				'required':'Anda harus mengisi nama obat'
			},

			'jenis_obat':{
				'required':'Anda harus memilih jenis obat'
			},
			'bentuk_obat':{
				'required':'Anda harus memilih bentuk obat'
			},
			'harga_obat':{
				'required':'Anda harus mengisi harga obat'
			},

			'stock_obat':{
				'required':'Anda harus mengisi stock obat'
			},
			'kode_suplier':{
				'required':'Anda harus memilih suplier'
			}
		}