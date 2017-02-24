from django.contrib import admin

from Pemesanan.models import*
# Register your models here.

class Admin_Pemesanan(admin.ModelAdmin):

    list_display = ['kode_pemesanan','tanggal_pemesanan','kode_pelanggan','kode_karyawan']
    search_fields = ['kode_pemesanan','kode_karyawan']
    list_per_page = 15

admin.site.register(Pemesanan, Admin_Pemesanan)
