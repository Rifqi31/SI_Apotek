from django.forms import ModelForm
from django import forms

from Pelanggan.models import*

class Pelanggan_Form(ModelForm):

	class Meta:

		model = Pelanggan
		fields = ['nama_pelanggan','alamat_pelanggan','nomer_telepon']
		labels = {

			'nama_pelanggan':'Nama Pelanggan',
			'alamat_pelanggan':'Alamat',
			'nomer_telepon':'Nomer Telepon'
		}

		error_messages = {

			'nama_pelanggan':{
				'required':'Anda harus mengisi nama'
			},
			'alamat_pelanggan':{
				'required':'Anda harus mengisi alamat'
			},
			'nomer_telepon':{
				'required':'Anda haru mengisi nomer telepon'
			}

		}

		widget = {
			'alamat_pelanggan':forms.Textarea(attrs = {'col':60,'row':10})
		}