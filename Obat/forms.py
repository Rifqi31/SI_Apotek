from django.forms import ModelForm
from django import forms

from Obat.models import*

class Obat_Form(ModelForm):

	class Meta:

		model = Obat
		fields = ['nama_obat','jenis_obat','bentuk_obat','harga_obat','stock_obat']
		labels = {

			'nama_obat' : 'Nama Obat',
			'jenis_obat' : 'Jenis Obat',
			'bentuk_obat' : 'Bentuk Obat',
			'harga_obat' : 'Harga Obat',
			'stock_obat' : 'Stock'
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
			}
		}