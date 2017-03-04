from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

from random import randint
import random

from Resep.models import Data_Resep
from Resep.forms import Resep_Form

# Create your views here.
@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def Isi_Data_Resep(request):
    if request.method == 'POST':
        form = Resep_Form(request.POST)


        for x in range(1,100):
            kode_number = random.randint(1, 100000)
            kode_number += long(x)


        if form.is_valid():
            initial = form.save(commit = False)

            initial.kode_resep = kode_number
            initial.tanggal_resep = request.POST['tanggal_resep']
            initial.kode_pelanggan = form.cleaned_data.get('kode_pelanggan')
            initial.nama_pasien = initial.kode_pelanggan.nama_pelanggan
            
            initial.save()
            form.save()
            return redirect('/')

    else:
        form = Resep_Form()

    return render(request, 'resep.html',{'form':form})
