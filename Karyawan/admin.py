from django.contrib import admin

from Karyawan.models import*

import datetime

# Register your models here.

class Admin_Karyawan(admin.ModelAdmin):

    list_display = ['nama_karyawan','tanggal_lahir_karyawan','alamat_karyawan','telepon_karyawan','email_karyawan']
    search_fields = ['nama_karyawan','telepon_karyawan','email_karyawan']
    list_per_page = 15

admin.site.register(BiodataKaryawan, Admin_Karyawan)


class Admin_AkunKaryawan(admin.ModelAdmin):

    list_display = ['akun','karyawan','shift_kerja']
    search_fields = ['akun','karyawan','shift_kerja']
    list_per_page = 15

admin.site.register(Akun_karyawan, Admin_AkunKaryawan)


class Admin_AbsenKaryawan(admin.ModelAdmin):

	list_display = ['karyawan','jenis_kehadiran','waktu','shift_kerja_karyawan']
	list_filter = ['jenis_kehadiran','shift_kerja_karyawan']
	search_fields = ['karyawan']
	list_per_page = 15

admin.site.register(Absen_karyawan, Admin_AbsenKaryawan)


class Admin_IzinKaryawan(admin.ModelAdmin):
	list_display = ['karyawan','jenis_kehadiran','waktu_mulai','waktu_berhenti','alasan','disetujui']
	search_fields = ['karyawan']
	list_per_page = 15

	actions = ['setuju_izin','batalkan_izin']

	def setuju_izin(self, request, queryset):
		for izin in queryset:
			diff = izin.waktu_berhenti - izin.waktu_mulai
			base = izin.waktu_berhenti
			numdays = diff.days + 1
			date_list = [base - datetime.timedelta(days = x)for x in range(0, numdays)]

			for date in date_list:
				print date
				isi_absen_karyawan = Absen_karyawan(
					
					karyawan = izin.karyawan,
					jenis_kehadiran = izin.jenis_kehadiran,
					waktu = date 
					
					)
				Absen_karyawan.save()

			izin.disetujui = True
			izin.save()

	setuju_izin.short_description = "Terima pengajuan izin yang dipilih"

	def batalkan_izin(self, request, queryset):
		queryset.update(disetujui = False)

	batalkan_izin.short_description = "Batalkan pengajuan yang dipilih"
	

admin.site.register(Izin_karyawan, Admin_IzinKaryawan)