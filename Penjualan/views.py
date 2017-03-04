from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Sum

from Penjualan.models import Data_Penjualan
from Pemesanan.models import DetailPemesanan

import random


# Create your views here.
@login_required(login_url=settings.LOGIN_KARYAWAN_URL)
def hitung_penjualan(request):
    if request.POST:
        try:
            for x in range(1, 100):
                kode_number = random.randint(1, 100000)
                kode_number += long(x)

            jumlah = DetailPemesanan.objects.all().aggregate(Sum('jumlah'))
            total_harga_perobat = DetailPemesanan.objects.all().aggregate(Sum('total_harga_perobat'))

            isi_penjualan = Data_Penjualan(

                kode_penjualan=kode_number,
                kode_pemesanan=DetailPemesanan.objects.get(id=1),
                nama_pelanggan=kode_number.nama_pemesan,
                total_barang=jumlah['jumlah__sum'],
                total_penjualan=total_harga_perobat['total_harga_perobat__sum']
            )
            isi_penjualan.save()
            return redirect('/')
        except:
            raise Http404("Wrong Code")

    return render(request, 'penjualan.html')
