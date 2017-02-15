from django.shortcuts import render, redirect
from django.conf import settings

from random import randint
import random

# models and forms
from suplier.models import suplier, pembelian_obat, detail_pembelian_obat
from suplier.forms import suplier_form, pembelian_obat_form, pembelian_detail_form

# Create your views here.

def data_suplier(request):
	if request.method == 'POST':
		form_data = request.POST
		form = suplier_form(form_data)

		if form.is_valid():

			#random number for primary key
			for x in range(1,100):
				number = random.randint(1, 10000000000)
				number += long(x)

				kode_number = number

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

			#random number for primary key
			for x in range(1,100):
				number = random.randint(1, 10000000000)
				number += long(x)

				kode_number = number

			input_pembelian = pembelian_obat(
				
				kd_pembelian = kode_number,
				kd_suplier_obat =  form.cleaned_data.get('kd_suplier_obat'),
				total_pembelian = form.cleaned_data.get('total_pembelian')
				
				)
			input_pembelian.save()
			return redirect('/')
	else:
		form = pembelian_obat_form()

	return render(request, 'pembelian.html',{'form':form})


def data_pembelian_obat_detail(request):
	if request.method == 'POST':
		form_data = request.POST
		form = pembelian_detail_form(form_data)

		if form.is_valid():

			input_detail_pembelian = detail_pembelian_obat(
				
				kd_pembelian_detail =  form.cleaned_data.get('kd_pembelian_detail'),
				kd_obat_detail =  form.cleaned_data.get('kd_obat_detail'),
				jumlah_beli = request.POST['jumlah_beli'],
				total_harga_perobat = form.cleaned_data.get('total_harga_perobat')
				
				)
			input_detail_pembelian.save()
			return redirect('/')
	else:
		form = pembelian_detail_form()

	return render(request, 'pembelian_detail.html',{'form':form})
