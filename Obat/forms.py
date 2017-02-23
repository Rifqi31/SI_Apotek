from django.forms import ModelForm
from django import forms

from Obat.models import*

class Obat_Form(ModelForm):

	class Meta:

		model = Obat
		fields = ['nama_obat','kode_jenis_obat','harga_obat','stock_obat']
		labels = {

			'nama_obat' : 'Nama Obat',
			'kode_jenis_obat' : 'Kode Jenis Obat',
			'harga_obat' : 'Harga Obat',
			'stock_obat' : 'Stock'
		}

		error_messages = {

			'nama_obat':{
				'required':'Anda harus mengisi nama obat'
			},

			'kode_jenis_obat':{
				'required':'Anda harus memilih kode jenis obat'
			},

			'harga_obat':{
				'required':'Anda harus mengisi harga obat'
			},

			'stock_obat':{
				'required':'Anda harus mengisi stock obat'
			}
		}


class JenisObat_Form(ModelForm):

	class Meta:

		model = JenisObat 
		fields = ['nama_jenis_obat']
		labels = {

			'nama_jenis_obat' : 'Jenis Obat'
		}

		error_messages = {

			'nama_jenis_obat':{
				'required':'Anda harus memilih nama jenis obat'
			}				
		}