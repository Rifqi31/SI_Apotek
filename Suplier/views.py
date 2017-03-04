from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import random

from Suplier.models import Data_Suplier
from Suplier.forms import Data_Suplier_Form


# Create your views here.

@login_required(login_url=settings.LOGIN_KARYAWAN_URL)
def isi_data_suplier(request):
    if request.method == 'POST':
        form = Data_Suplier_Form(request.POST)

        for x in range(1, 100):
            kode_number = random.randint(1, 100000)
            kode_number += long(x)

        if form.is_valid():
            suplier = Data_Suplier(

                kode_suplier=kode_number,
                nama_suplier=request.POST['nama_suplier'],
                alamat_suplier=request.POST['alamat_suplier'],
                telepon_suplier=request.POST['telepon_suplier'],
                email_suplier=request.POST['email_suplier'],
            )
            suplier.save()
            return redirect('/')

    else:
        form = Data_Suplier_Form()

    return render(request, 'suplier.html', {'form': form})


@login_required(login_url=settings.LOGIN_KARYAWAN_URL)
def tampil_daftar_suplier(request):
    daftar_suplier = Data_Suplier.objects.all()
    # pagination
    paginator = Paginator(daftar_suplier, 5)
    page = request.GET.get('page')
    try:
        daftar_suplier = paginator.page(page)
    except PageNotAnInteger:
        daftar_suplier = paginator.page(1)
    except EmptyPage:
        daftar_suplier = paginator.page(paginator.num_pages)

    return render(request, 'daftar_suplier.html', {'daftar_suplier': daftar_suplier})
