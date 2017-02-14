from django.shortcuts import render, redirect
from django.conf import settings

from random import randint
import random

# models and forms
from costumer.models import costumer
from costumer.forms import costumer_form

# Create your views here.

def data_costumer(request):
	if request.method == 'POST':
		form_data = request.POST
		form = costumer_form(form_data)

		if form.is_valid():

			#count at zero for length data
			kode_number = random.randint(1, 10000000000)

			input_costumer = costumer(
				
				kd_costumer = kode_number,
				nama_costumer = request.POST['nama_costumer'],
				alamat_costumer = request.POST['alamat_costumer']
				
				)
			input_costumer.save()
			return redirect('/')
	else:
		form = costumer_form()

	return render(request, 'costumer.html',{'form':form})





def homepage(request):

	return render(request, 'homepage.html',{})