from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Sum

import random

from Transaksi.forms import*
from Transaksi.models import*
from Costumer.models import*

# Create your views here.
@login_required(login_url=settings.LOGIN_KARYAWAN_URL)
def isi_data_pembelian(request):
    if request.method == 'POST':
        form = Data_Pembelian_Form(request.POST)

        for x in range(1, 100):
            kode_number = random.randint(1, 100000)
            kode_number += long(x)

        if form.is_valid():
            initial = form.save(commit=False)

            initial.kode_pembelian = kode_number
            initial.kode_suplier = form.cleaned_data.get('kode_suplier')
            initial.nama_suplier = initial.kode_suplier.nama_suplier
            initial.nama_obat = request.POST['nama_obat']
            initial.harga_beli = form.cleaned_data.get('harga_beli')
            initial.total_barang = request.POST['total_barang']
            initial.total_pembelian = initial.harga_beli * initial.total_barang

            initial.save()
            form.save()
            return redirect('/')

    else:
        form = Data_Pembelian_Form()

    return render(request, 'pembelian.html', {'form': form})


@login_required(login_url=settings.LOGIN_KARYAWAN_URL)
def hitung_penjualan(request):
    if request.method == 'POST':
        form = Data_Penjualan_Form(request.POST)

        for x in range(1, 100):
            kode_number = random.randint(1, 100000)
            kode_number += long(x)

        if form.is_valid():
            initial = form.save(commit=False)

            initial.kode_penjualan = kode_number
            initial.nama_pemesan = DetailPemesanan.objects.get(id=1)
            initial.nama_pelanggan = initial.nama_pemesan.nama_pemesan

            jumlah = DetailPemesanan.objects.all().aggregate(Sum('jumlah'))
            initial.total_barang = jumlah['jumlah__sum']

            total_harga_perobat = DetailPemesanan.objects.all().aggregate(Sum('total_harga_perobat'))
            initial.total_penjualan = total_harga_perobat['total_harga_perobat__sum']

            initial.save()
            form.save()
            return redirect('/')

    else:
        form = Data_Penjualan_Form()

    return render(request, 'penjualan.html', {'form': form})

