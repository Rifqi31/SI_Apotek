from django.contrib import admin

from Karyawan.models import*
# Register your models here.

class Admin_Karyawan(admin.ModelAdmin):

    list_display = ['kode_karyawan','nama_karyawan','tanggal_lahir_karyawan','alamat_karyawan','telepon_karyawan','email_karyawan']
    search_fields = ['nama_karyawan','kode_karyawan','telepon_karyawan','email_karyawan']
    list_per_page = 15

admin.site.register(BiodataKaryawan, Admin_Karyawan)

class Admin_AkunKaryawan(admin.ModelAdmin):

    list_display = ['akun','kode_karyawan']
    search_fields = ['akun','kode_karyawan']
    list_per_page = 15

admin.site.register(Akun_karyawan, Admin_AkunKaryawan)
