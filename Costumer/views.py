from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
import random

from Costumer.models import*
from Costumer.forms import*
from Karyawan.models import Biodata_karyawan
# Create your views here.

@login_required(login_url=settings.LOGIN_KARYAWAN_URL)
def isi_data_pelanggan(request):
    if request.method == 'POST':
        form = Data_Pelanggan_Form(request.POST)

        for x in range(1, 100):
            kode_number = random.randint(1, 100000)
            kode_number += long(x)

        if form.is_valid():
            pelanggan = Data_Pelanggan(

                kode_pelanggan=kode_number,
                nama_pelanggan=request.POST['nama_pelanggan'],
                alamat_pelanggan=request.POST['alamat_pelanggan'],
                nomer_telepon=request.POST['nomer_telepon']
            )
            pelanggan.save()
            return redirect('/')

    else:
        form = Data_Pelanggan_Form()

    return render(request, 'pelanggan.html', {'form': form})

@login_required(login_url=settings.LOGIN_KARYAWAN_URL)
def isi_data_pemesanan(request):
    if request.method == 'POST':
        form = Data_Pemesanan_Form(request.POST)

        for x in range(1, 100):
            kode_number = random.randint(1, 100000)
            kode_number += long(x)

        if form.is_valid():
            initial = form.save(commit=False)

            initial.kode_pemesanan = kode_number
            initial.kode_pelanggan = form.cleaned_data.get('kode_pelanggan')
            initial.nama_pelanggan = initial.kode_pelanggan.nama_pelanggan
            initial.karyawan = Biodata_karyawan.objects.get(id=request.session['karyawan_id'])

            initial.save()
            form.save()
            return redirect('/')

    else:
        form = Data_Pemesanan_Form()

    return render(request, 'pemesanan.html', {'form': form})



@login_required(login_url=settings.LOGIN_KARYAWAN_URL)
def data_detailpemesanan(request):
    if request.method == 'POST':
        form = DetailPemesanan_Form(request.POST)

        if form.is_valid():
            initial = form.save(commit=False)

            initial.kode_pemesanan = form.cleaned_data.get('kode_pemesanan')
            initial.nama_pemesan = initial.kode_pemesanan.nama_pelanggan
            initial.kode_obat = form.cleaned_data.get('kode_obat')
            initial.nama_obat = initial.kode_obat.nama_obat
            initial.kode_resep = form.cleaned_data.get('kode_resep')
            initial.jumlah = request.POST['jumlah']
            initial.total_harga_perobat = initial.kode_obat.harga_obat * initial.jumlah

            initial.save()
            form.save()
            return redirect('/')

    else:
        form = DetailPemesanan_Form()

    return render(request, 'detail_pemesanan.html', {'form': form})