from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

#Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Reportlab
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.lib.units import inch
from reportlab.lib import colors

#import models
from Karyawan.models import Biodata_Karyawan, Akun_karyawan, Absen_karyawan, Izin_karyawan
from Karyawan.forms import Karyawan_Form, Izin_karyawan_Form #,akun_form

#import random
from random import randint
import random

# Create your views here.
def login_karyawan_view(request):
	if request.POST:
		user = authenticate(username=request.POST['username'],password=request.POST['password'])

		if user is not None:
			if user.is_active:
				try:
					akun = Akun_karyawan.objects.get(akun = user.id)

					login(request, user)

					#login with auto absen
					Absen_karyawan.objects.create(karyawan = akun, jenis_kehadiran = "hadir")

					request.session['karyawan_id'] = akun.karyawan.id
					request.session['username'] = request.POST['username']

				except:
					messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data karyawan, silahkan hubungi administartor')
				return redirect('/')

			else:
				messages.add_message(request, messages.INFO, 'User belum terverifikasi')

		else:
			messages.add_message(request, messages.INFO, 'Username atau password Anda salah')

	return render(request, 'login_karyawan.html')




@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def logout_karyawan_view(request):
	logout(request)
	return redirect('/')




#register karyawan baru
def register_karyawan(request):
	if request.method == 'POST':
		form = Karyawan_Form(request.POST)

		if form.is_valid():
			isi_data_karyawan = Biodata_Karyawan(

				nama_karyawan = request.POST['nama_karyawan'],
				tanggal_lahir = request.POST['tanggal_lahir'],
				alamat = request.POST['alamat'],
				telepon= request.POST['telepon'],
				email_karyawan = request.POST['email_karyawan'],
				shift_kerja = request.POST['shift_kerja']

				)
			isi_data_karyawan.save()
			return redirect('/')
	
	else:
		form = Karyawan_Form()

	return render(request, 'register_karyawan.html',{'form':form})



#def register_user_view(request):
#	if request.method == 'POST':
#		form_data = request.POST
#		form = akun_form(form_data)

#		if form.is_valid():

#			new_user = User.objects.create_user(**form.cleaned_data)


#			return redirect('/register_bio/')
#	else:
#		form = akun_form()

#	return render(request, 'register_bio.html',{'form':form})


@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def pengajuan_izin_karyawan(request):
	if request.method == 'POST':
		form = Izin_Karyawan_Form(request.POST)

		if form.is_valid():
			izin = Izin_karyawan(

				nama_karyawan = Biodata_Karyawan.objects.get(id = request.session['karyawan_id']),
				jenis_kehadiran = request.POST['jenis_kehadiran'],
				waktu_mulai = form.cleaned_data.get('waktu_mulai'),
				waktu_berhenti = request.POST['waktu_berhenti'],
				alasan = request.POST['alasan'],
				disetujui = False

				)
			izin.save()
			return redirect('/')

	else:
		form = Izin_Karyawan_Form()

	return render(request, 'tambah_izin.html', {'form':form})




@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def daftar_hadir_karyawan(request):
	daftar_hadir = None

	bulan = 0
	tahun = 0

	if request.method == 'POST':
		bulan = request.POST['bulan']
		tahun = request.POST['tahun']
		daftar_hadir = Absen_karyawan.objects.filter(waktu__year = tahun, waktu__month = bulan, karyawan__id = request.session['karyawan_id'])

	return render(request, 'daftar_hadir.html',{'daftar_hadir':daftar_hadir, 'bulan':bulan, 'tahun':tahun})




@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def daftar_izin_karyawan(request):
	daftar_izin = Izin_karyawan.objects.filter(karyawan__id = request.session['karyawan_id']).order_by('waktu_mulai')

	#pagination
	paginator = Paginator(daftar_izin, 5)
	page = request.GET.get('page')
	try:
		daftar_izin = paginator.page(page)
	except PageNotAnInteger:
		daftar_izin = paginator.page(1)
	except EmptyPage:
		daftar_izin = paginator.page(paginator.num_pages)

	return render(request, 'daftar_izin.html',{'daftar_izin':daftar_izin})





@login_required(login_url=settings.LOGIN_KARYAWAN_URL)
def cetak_absensi(request, bulan, tahun):
	#pengaturan respon berformat pdf
	filename = "daftar_hadir_" + str(bulan) + "_" + str(tahun)
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition']='attachment;filename="' + filename + '.pdf"'

	#mengambil daftar kehadiran dan mengubahnya menjadi data untuk tabel
	data = Absen_karyawan.objects.filter(waktu__year=tahun, waktu__month=bulan, karyawan__id=request.session['karyawan_id'])

	
	table_data = []
	table_data.append(["Tanggal","Status"])
	for x in data:
		table_data.append([ x.waktu, x.jenis_kehadiran ])

	#membuat dokumen baru
	doc = SimpleDocTemplate(response, pagesizes=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
	styles = getSampleStyleSheet()

	#pengaturan tabel di pdf
	table_style = TableStyle([
					('ALIGN',(1,1),(-2,-2),'RIGHT'),
					('FONT',(0,0),(-1,0),'Helvetica-Bold'),
					('VALIGN',(0,0),(0,-1),'TOP'),
					('INNERGRID',(0,0),(-1,-1),0.25,colors.black),
					('BOX',(0,0),(-1,-1),0.25,colors.black),
		])
	kehadiran_table= Table(table_data, colWidths=[doc.width/4.0]*2)
	kehadiran_table.setStyle(table_style)

	#mengisi pdf
	content = []
	content.append(Paragraph('Daftar Kehadiran %s%s' % (bulan, tahun), styles['Title']))
	content.append(Spacer(1,12))
	content.append(Paragraph('Berikut ini adalah hasil rekam jejak kehadiran Anda selama bulan %s tahun %s:' % (bulan, tahun), styles['Normal']))
	content.append(Spacer(1,12))
	content.append(kehadiran_table)
	content.append(Spacer(1,36))
	content.append(Paragraph('Mengetahui,',styles['Normal']))
	content.append(Spacer(1,48))
	content.append(Paragraph('Rifqi Muttaqin, Head of Departement PT.iDEA Development.',styles['Normal']))

	#menghasilkan pdf untuk di download
	doc.build(content)
	return response