from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Sum

from Penjualan.models import Data_Penjualan
from Penjualan.forms import Data_Penjualan_Form
from Pemesanan.models import DetailPemesanan

import random


# Create your views here.
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
            initial.kode_pemesanan = DetailPemesanan.objects.get(id=1)
            initial.nama_pelanggan = initial.kode_pemesanan.nama_pemesan

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
