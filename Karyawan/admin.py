from __future__ import print_function
from django.contrib import admin

from Karyawan.models import Biodata_karyawan, Akun_karyawan, Absen_karyawan, Izin_karyawan

import datetime


# Register your models here.
class Admin_Karyawan(admin.ModelAdmin):
    list_display = ['nama_karyawan', 'tanggal_lahir', 'alamat', 'telepon', 'email_karyawan', 'shift_kerja']
    list_filter = ['shift_kerja']
    search_fields = ['nama_karyawan', 'telepon', 'email_karyawan']
    list_per_page = 15


admin.site.register(Biodata_karyawan, Admin_Karyawan)


class Admin_Akun_Karyawan(admin.ModelAdmin):
    list_display = ['akun', 'karyawan']
    search_fields = ['akun', 'karyawan']
    list_per_page = 15


admin.site.register(Akun_karyawan, Admin_Akun_Karyawan)


class Admin_Absen_Karyawan(admin.ModelAdmin):
    list_display = ['karyawan', 'jenis_kehadiran', 'waktu']
    list_filter = ['jenis_kehadiran']
    search_fields = ['karyawan']
    list_per_page = 15


admin.site.register(Absen_karyawan, Admin_Absen_Karyawan)


class Admin_Izin_Karyawan(admin.ModelAdmin):
    list_display = ['karyawan', 'jenis_kehadiran', 'waktu_mulai', 'waktu_berhenti', 'alasan', 'disetujui']
    search_fields = ['karyawan']
    list_per_page = 15

    actions = ['setuju_izin', 'batalkan_izin']

    def setuju_izin(self, queryset):
        for izin in queryset:
            diff = izin.waktu_berhenti - izin.waktu_mulai
            base = izin.waktu_berhenti
            numdays = diff.days + 1
            date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]

            for date in date_list:
                print(date)
                isi_absen_karyawan = Absen_karyawan(

                    karyawan=izin.karyawan,
                    jenis_kehadiran=izin.jenis_kehadiran,
                    waktu=date

                )
                isi_absen_karyawan.save()

            izin.disetujui = True
            izin.save()

    setuju_izin.short_description = "Terima pengajuan izin yang dipilih"

    def batalkan_izin(self, queryset):
        queryset.update(disetujui=False)

    batalkan_izin.short_description = "Batalkan pengajuan yang dipilih"


admin.site.register(Izin_karyawan, Admin_Izin_Karyawan)
