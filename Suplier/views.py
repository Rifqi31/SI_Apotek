from django.shortcuts import render
from django.conf import settings

from Suplier.models import*
from Suplier.forms import*

# Create your views here.
def Data_Suplier(request):
    if request.method == 'POST':
        form = Suplier_Form(request.POST)


        for x in range(1,100):
            kode_number = random.randint(1, 100000)
            kode_number += long(x)


        if form.is_valid():
            isi_data_suplier = Suplier(

                kode_suplier = kode_number,
                nama_suplier = request.POST['nama_suplier'],
                alamat_suplier = request.POST['alamat_supleir'],
                telepon_suplier = request.POST['telepon_supleir'],
                email_suplier = request.POST['email_supleir'],
                )
            isi_data_suplier.save()
            return redirect('/')

    else:
        form = Suplier_Form()

    return render(request, 'suplier.html',{'form':form})
