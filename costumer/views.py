from django.shortcuts import render, redirect
from django.conf import settings

from random import randint
import random

# models and forms
from costumer.models import costumer, penjualan_obat, detail_penjualan_obat
from costumer.forms import costumer_form, penjualan_obat_form, penjualan_detail_form

# Create your views here.

def data_costumer(request):
	if request.method == 'POST':
		form_data = request.POST
		form = costumer_form(form_data)

		if form.is_valid():

			#random number for primary key
			for x in range(1,100):
				number = random.randint(1, 10000000000)
				number += long(x)

				kode_number = number


			input_costumer = costumer(
				
				kd_costumer = kode_number,
				nama_costumer = request.POST['nama_costumer'],
				alamat_costumer = request.POST['alamat_costumer']
				
				)
			input_costumer.save()
			return redirect('/')
	else:
		form = costumer_form()

	return render(request, 'costumer.html',{'form':form})


def data_penjualan_obat(request):
	if request.method == 'POST':
		form_data = request.POST
		form = penjualan_obat_form(form_data)

		if form.is_valid():

			#random number for primary key
			for x in range(1,100):
				number = random.randint(1, 10000000000)
				number += long(x)

				kode_number = number

			input_penjualan = penjualan_obat(
				
				kd_penjualan = kode_number,
				kd_costumer =  form.cleaned_data.get('kd_costumer'),
				tgl_penjualan = request.POST['tgl_penjualan'],
				total_penjualan = request.POST['total_penjualan']
				
				)
			input_penjualan.save()
			return redirect('/')
	else:
		form = penjualan_obat_form()

	return render(request, 'penjualan.html',{'form':form})


def data_penjualan_obat_detail(request):
	if request.method == 'POST':
		form_data = request.POST
		form = penjualan_detail_form(form_data)

		if form.is_valid():

			input_detail_penjualan = detail_penjualan_obat(
				
				kd_penjualan_detail = form.cleaned_data.get('kd_penjualan_detail'),
				kd_obat_detail =  form.cleaned_data.get('kd_obat_detail'),
				jumlah_jual = request.POST['jumlah_jual'],
				total_harga_perobat = form.cleaned_data.get('total_harga_perobat')
				
				)
			input_detail_penjualan.save()
			return redirect('/')
	else:
		form = penjualan_detail_form()

	return render(request, 'penjualan_detail.html',{'form':form})




def homepage(request):

	return render(request, 'homepage.html',{})