from django.shortcuts import render,redirect
from django.conf import settings

from random import randint
import random

from Pemesanan.models import*

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
