from django.shortcuts import render, redirect
from django.conf import settings

from random import randint
import random

from Pelanggan.models import*
from Pelanggan.forms import*

# Create your views here.

def Data_Pelanggan(request):
	if request.method == 'POST':
		form = Pelanggan_Form(request.POST)

		for x in range(1,100):
			kode_number = random.randint(1, 100000)
			kode_number += long(x)

		if form.is_valid():
			isi_data_pelanggan = Pelanggan(

				kode_pelanggan = kode_number,
				nama_pelanggan = request.POST['nama_pelanggan'],
				alamat_pelanggan = request.POST['alamat_pelanggan'],
				nomer_telepon = request.POST['nomer_telepon']
				)
			isi_data_pelanggan.save()
			return redirect('/')

	else:
		form = Pelanggan_Form()

	return render(request, 'pelanggan.html',{'form':form})
