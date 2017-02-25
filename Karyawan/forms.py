from django.forms import ModelForm
from django import forms

from Karyawan.models import*

class Karyawan_Form(ModelForm):

	class Meta:

		model = BiodataKaryawan
		fields = ['nama_karyawan','tanggal_lahir_karyawan','alamat_karyawan','telepon_karyawan','email_karyawan']
		labels = {

			'nama_karyawan' : 'Nama Lengkap',
			'tanggal_lahir_karyawan' : 'Tanggal Lahir',
			'alamat_karyawan' : 'Alamat',
			'telepon_karyawan' : 'Nomer Telepon',
			'email_karyawan' : 'Email'
		}

		error_messages = {

			'nama_karyawan':{
				'required':'Anda harus mengisi nama'
			},

			'tanggal_lahir_karyawan':{
				'required':'Anda harus mengisi tanggal lahir'
			},

			'alamat_karyawan':{
				'required':'Anda harus mengisi alamat'
			},
			'telepon_karyawan':{
				'required':'Anda harus mengisi nomer telepon'
			}
		}