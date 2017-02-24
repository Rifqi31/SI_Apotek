from django.shortcuts import render
from django.conf import settings

from Resep.models import*
from Resep.forms import*

# Create your views here.
def Data_Resep(request):
    if request.method == 'POST':
        form = Resep_Form(request.POST)


        for x in range(1,100):
            kode_number = random.randint(1, 100000)
            kode_number += long(x)


        if form.is_valid():
            isi_data_resep = Resep(

                kode_resep = kode_number,
                tanggal_resep = request.POST['tanggal_resep'],
                nama_pasien = request.POST['nama_pasien'],
                )
            isi_data_resep.save()
            return redirect('/')

    else:
        form = Resep_Form()

    return render(request, 'resep.html',{'form':form})
