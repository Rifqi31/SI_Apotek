from django.forms import ModelForm
from django import forms

from costumer.models import costumer, penjualan_obat, detail_penjualan_obat

class costumer_form(ModelForm):
	class Meta:

		model = costumer
		fields = ['nama_costumer','alamat_costumer']
		labels = {

			'nama_costumer' : 'Nama',
			'alamat_costumer' : 'Alamat',
		}

		error_messages = {

			'nama_costumer':{
				'required':'Anda harus mengisi nama'
			},

			'alamat_costumer':{
				'required':'Anda harus mengisi alamat'
			}
		}

		widget = {

			'Alamat':forms.Textarea(attrs = {'col':60,'row':10})
		}


class penjualan_obat_form(ModelForm):
	class Meta:

		model = penjualan_obat
		fields = ['kd_costumer_obat','total_penjualan']
		labels = {

			'kd_costumer_obat' : 'Kode Costumer',
			'total_penjualan' : 'Total Penjualan'
		}

		error_messages = {

			'kd_costumer_obat':{
				'required':'Anda harus memilih kode costumer'
			},
			
			'total_penjualan':{
				'required':'Anda harus mengisi total penjualan'
			}
		}

class penjualan_detail_form(ModelForm):
	class Meta:

		model = detail_penjualan_obat
		fields = ['kd_penjualan_detail','kd_obat_detail','jumlah_jual','total_harga_perobat']
		labels = {

			'kd_penjualan_detail' : 'Kode Penjualan',
			'kd_obat_detail' : 'Kode Obat',
			'jumlah_penjualan' : 'Jumlah Penjualan',
			'total_harga_perobat' : 'Total harga'
		}

		error_messages = {

			'kd_penjualan_detail':{
				'required':'Anda harus memilih kode penjualan'
			},

			'kd_obat_detail':{
				'required':'Anda harus memilih kode obat'
			},

			'jumlah_penjualan':{
				'required':'Anda harus mengisi jumlah penjualan'
			},

			'total_harga_perobat':{
				'required':'Anda harus mengisi total_harga'
			}		
		}
