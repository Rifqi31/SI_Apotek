from django.forms import ModelForm
from django import forms

from suplier.models import suplier, pembelian_obat, detail_pembelian_obat

class suplier_form(ModelForm):
	class Meta:

		model = suplier
		fields = ['nama_suplier','alamat_suplier']
		labels = {

			'nama_suplier' : 'Nama',
			'alamat_suplier' : 'Alamat'
		}

		error_message = {

			'nama_suplier':{
				'required':'Anda harus mengisi nama'
			},
			'alamat_suplier':{
				'required':'Anda harus mengisi alamat'
			},

		}
		widget = {

			'Alamat':forms.Textarea(attrs = {'col':60,'row':10})
		}


class pembelian_obat_form(ModelForm):
	class Meta:

		model = pembelian_obat
		fields = ['kd_suplier_obat','tgl_pembelian','total_pembelian']
		labels = {

			'kd_suplier_obat' : 'Kode Suplier',
			'tgl_pembelian' : 'Tanggal Pembelian',
			'total_pembelian' : 'Total Pembelian'
		}

		error_message = {

			'kd_suplier_obat':{
				'required':'Anda harus memilih suplier'
			},
			
			'tgl_pembelian':{
				'required':'Anda harus mengisi tanggal'
			},

			'total_pembelian':{
				'required':'Anda harus mengisi total'
			},

		}

class pembelian_detail_form(ModelForm):
	class Meta:

		model = detail_pembelian_obat
		fields = ['kd_pembelian_detail','kd_obat_detail','jumlah_beli','total_harga_perobat']
		labels = {

			'kd_pembelian_detail' : 'Kode Pembelian',
			'kd_obat_detail' : 'Kode Obat',
			'jumlah_beli' : 'Jumlah Beli',
			'total_harga_perobat' : 'Total Harga'
		}

		error_message = {

			'kd_pembelian_obat':{
				'required':'Anda harus memilih kode pembelian'
			},
			'kd_obat_detail':{
				'required':'Anda harus memilih kode obat'
			},
			'jumlah_beli':{
				'required':'Anda harus mengisi jumlah beli'
			},
			'total_pembelian':{
				'required':'Anda harus mengisi total pembelian'
			}
		}