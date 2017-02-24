from django.shortcuts import render,redirect
from django.conf import settings

from random import randint
import random

from Pemesanan.models import*
from Pemesanan.forms import*

# Create your views here.

def Data_Pemesanan(request):
    if request.method == 'POST':
        form = Pemesanan_Form(request.POST)


        for x in range(1,100):
            kode_number = random.randint(1, 100000)
            kode_number += long(x)


        if form.is_valid():
            isi_data_pemesanan = Pemesanan(

                kode_pemesanan = kode_number,
                kode_pelanggan = form.cleaned_data.get('kode_pelanggan'),
                kode_karyawan = form.cleaned_data.get('kode_karyawan'),
                )
            isi_data_pemesanan.save()
            return redirect('/')

    else:
        form = Pemesanan_Form()

    return render(request, 'pemesanan.html',{'form':form})



def Data_DetailPemesanan(request):
    if request.method == 'POST':
        form = DetailPemesanan_Form(request.POST)

        if form.is_valid():
            isi_data_detail_pemesanan = DetailPemesanan(

                kode_pemesanan = form.cleaned_data.get('kode_pemesanan'),
                kode_obat = form.cleaned_data.get('kode_obat'),
                kode_resep = form.cleaned_data.get('kode_resep'),
                jumlah = request.POST['jumlah']
                )
            isi_data_detail_pemesanan.save()
            return redirect('/')

    else:
        form = DetailPemesanan_Form()

    return render(request, 'detail_pemesanan.html',{'form':form})
