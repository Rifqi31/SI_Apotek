from django.forms import ModelForm
from django import forms

from Suplier.models import*

class Suplier_Form(ModelForm):

	class Meta:

		model = Suplier
		fields = ['nama_suplier','alamat_suplier','telepon_suplier','email_suplier']
		labels = {

			'nama_suplier':'Nama Suplier',
			'alamat_suplier':'Alamat',
			'telepon_suplier':'Telepon',
			'email_suplier':'Email'
		}

		error_messages = {

			'nama_suplier':{
				'required':'Anda harus mengisi nama'
			},
			'alamat_suplier':{
				'required':'Anda harus mengisi alamat'

			},
			'telepon_suplier':{
				'required':'Anda harus mengisi nomer telepon'

			},
			'email_suplier':{
				'required':'Anda harus mengisi email'

			}
		}