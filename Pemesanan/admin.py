from django.contrib import admin

from Pemesanan.models import*
# Register your models here.

class Admin_Pemesanan(admin.ModelAdmin):

    list_display = ['kode_pemesanan','tanggal_pemesanan','kode_pelanggan','kode_karyawan']
    search_fields = ['kode_pemesanan','kode_karyawan']
    list_per_page = 15

admin.site.register(Pemesanan, Admin_Pemesanan)


class Admin_DetailPemesanan(admin.ModelAdmin):

    list_display = ['kode_pemesanan','kode_obat','kode_resep','jumlah']
    search_fields = ['kode_pemesanan','kode_obat','kode_resep']
    list_per_page = 15

admin.site.register(DetailPemesanan, Admin_DetailPemesanan)
