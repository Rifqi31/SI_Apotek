from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

#import models
from Karyawan.models import*
from Karyawan.forms import*

# Create your views here.

def login_karyawan_view(request):
	if request.POST:
		user = authenticate(username=request.POST['username'],password=request.POST['password'])

		if user is not None:
			if user.is_active:
				try:
					akun = Akun_karyawan.objects.get(akun=user.id)

					login(request, user)

					request.session['karyawan_id'] = akun.karyawan.id
					request.session['username'] = request.POST['username']

				except:
					messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data karyawan, silahkan hubungi administartor')
				return redirect('/')

			else:
				messages.add_message(request, messages.INFO, 'User belum terverifikasi')

		else:
			messages.add_message(request, messages.INFO, 'Username atau password Anda salah')

	return render(request, 'login_karyawan.html')


def logout_karyawan_view(request):
	logout(request)
	return redirect('/')


def register_karyawan(request):
	if request.method == 'POST':
		form = Karyawan_Form(request.POST)

		if form.is_valid():
			isi_data_karyawan = BiodataKaryawan(

				nama_karyawan = request.POST['nama_karyawan'],
				tanggal_lahir_karyawan = request.POST['tanggal_lahir_karyawan'],
				alamat_karyawan = request.POST['alamat_karyawan'],
				telepon_karyawan = request.POST['telepon_karyawan'],
				email_karyawan = request.POST['email_karyawan']

				)
			isi_data_karyawan.save()
			return redirect('/')
	
	else:
		form = Karyawan_Form()

	return render(request, 'register_karyawan.html',{'form':form})