from django.shortcuts import render,redirect
from django.conf import settings

from random import randint
import random

from Penjualan.models import*
from Penjualan.forms import*

# Create your views here.

def Data_Penjualan(request):
    if request.method == 'POST':
        form = Penjualan_Form(request.POST)


        for x in range(1,100):
            kode_number = random.randint(1, 100000)
            kode_number += long(x)


        if form.is_valid():
            isi_data_penjualan = Penjualan(

                kode_penjualan = kode_number,
                kode_pemesanan = form.cleaned_data.get('kode_pemesanan'),
                )
            isi_data_penjualan.save()
            return redirect('/')

    else:
        form = Penjualan_Form()

    return render(request, 'penjualan.html',{'form':form})
