from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

#Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from random import randint
import random

from Obat.models import Data_Obat
from Obat.forms import Data_Obat_Form
from Suplier.models import Data_Suplier

# Create your views here.
@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def Isi_Data_Obat(request):
	if request.method == 'POST':
		form = Data_Obat_Form(request.POST)

		for x in range(1,100):
			kode_number = random.randint(1, 100000)
			kode_number += long(x)


		if form.is_valid():
			initial = form.save(commit = False)

			initial.kode_obat = kode_number
			initial.nama_obat = request.POST['nama_obat']
			initial.jenis_obat = request.POST['jenis_obat']
			initial.bentuk_obat = request.POST['bentuk_obat']
			initial.harga_obat = form.cleaned_data.get('harga_obat')
			initial.stock_obat = request.POST['stock_obat']
			initial.kode_suplier = form.cleaned_data.get('kode_suplier')
			initial.nama_suplier = initial.kode_suplier.nama_suplier

			initial.save()
			form.save()
			return redirect('/')

	else:
		form = Data_Obat_Form()

	return render(request, 'obat.html',{'form':form})




#tampil daftar obat
@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def tampil_daftar_obat(request):
	daftar_obat = Data_Obat.objects.all()

	#pagination
	paginator = Paginator(daftar_obat, 5)
	page = request.GET.get('page')
	try:
		daftar_obat = paginator.page(page)
	except PageNotAnInteger:
		daftar_obat = paginator.page(1)
	except EmptyPage:
		daftar_obat = paginator.page(paginator.num_pages)

	return render(request, 'daftar_obat.html',{'daftar_obat':daftar_obat})




@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def homepage(request):

	return render(request, 'homepage.html',{})
