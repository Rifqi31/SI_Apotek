from django.shortcuts import render, redirect
from django.conf import settings

from random import randint
import random

# models and forms
from obat.models import obat
from obat.forms import obat_form

# Create your views here.

def data_obat(request):
	if request.method == 'POST':
		form_data = request.POST
		form = obat_form(form_data)

		if form.is_valid():

			#count at zero for length data
			kode_number = random.randint(1, 10000000000)

			input_obat = obat(
				
				kd_obat = kode_number,
				nama_obat = request.POST['nama_obat'],
				tipe_obat = request.POST['tipe_obat'],
				harga_jual = request.POST['harga_jual']
				
				)
			input_obat.save()
			return redirect('/')
	else:
		form = obat_form()

	return render(request, 'obat.html',{'form':form})