from django.forms import ModelForm
from django import forms

from costumer.models import costumer

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