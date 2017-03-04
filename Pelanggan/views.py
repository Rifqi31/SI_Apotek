from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

import random

from Pelanggan.models import Data_Pelanggan
from Pelanggan.forms import Data_Pelanggan_Form


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
