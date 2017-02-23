from django.shortcuts import render, redirect
from django.conf import settings

from random import randint
import random

from Obat.models import*
from Obat.forms import*

# Create your views here.

def Data_Obat(request):
	if request.method == 'POST':
		form = Obat_Form(request.POST)


	        for x in range(1,100):
				kode_number = random.randint(1, 100000)
				kode_number += long(x)


		if form.is_valid():
			isi_data_obat = Obat(

				kode_obat = kode_number,
				nama_obat = request.POST['nama_obat'],
				kode_jenis_obat = form.cleaned_data.get('kode_jenis_obat'),
				harga_obat = form.cleaned_data.get('harga_obat'),
				stock_obat = request.POST['stock_obat']

				)
			isi_data_obat.save()
			return redirect('/')

	else:
		form = Obat_Form()

	return render(request, 'obat.html',{'form':form})



def Data_JenisObat(request):
    if request.method == 'POST':
        form = JenisObat_Form(request.POST)

        for x in range(1,100):
			kode_number = random.randint(1, 100000)
			kode_number += long(x)

        if form.is_valid():
        
            initial = form.save(commit = False)
            initial.kode_jenis_obat = kode_number
            initial.nama_jenis_obat = request.POST['nama_jenis_obat']
            initial.save()
            
        form.save()
        return redirect('/')
   
    else:
        form = JenisObat_Form()

    return render(request, 'jenis_obat.html', {'form': form})



def homepage(request):

	return render(request, 'homepage.html',{})