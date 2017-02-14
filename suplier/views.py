from django.shortcuts import render, redirect
from django.conf import settings

from random import randint
import random

# models and forms
from suplier.models import suplier, pembelian_obat
from suplier.forms import suplier_form, pembelian_obat_form

# Create your views here.

def data_suplier(request):
	if request.method == 'POST':
		form_data = request.POST
		form = suplier_form(form_data)

		if form.is_valid():

			#count at zero for length data
			kode_number = random.randint(1, 10000000000)

			input_suplier = suplier(
				
				kd_suplier = kode_number,
				nama_suplier = request.POST['nama_suplier'],
				alamat_suplier = request.POST['alamat_suplier']
				
				)
			input_suplier.save()
			return redirect('/')
	else:
		form = suplier_form()

	return render(request, 'suplier.html',{'form':form})


def data_pembelian_obat(request):
	if request.method == 'POST':
		form_data = request.POST
		form = pembelian_obat_form(form_data)

		if form.is_valid():

			#count at zero for length data
			kode_number = random.randint(1, 10000000000)

			input_pembelian = pembelian_obat(
				
				kd_pembelian = kode_number,
				kd_suplier_obat =  form.cleaned_data.get('kd_suplier_obat'),
				tgl_pembelian = request.POST['tgl_pembelian'],
				total_pembelian = request.POST['total_pembelian']
				
				)
			input_pembelian.save()
			return redirect('/')
	else:
		form = pembelian_obat_form()

	return render(request, 'pembelian.html',{'form':form})


