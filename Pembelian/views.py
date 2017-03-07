from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

import random

from Pembelian.forms import Data_Pembelian_Form


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
