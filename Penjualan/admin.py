from django.contrib import admin

from Penjualan.models import*
# Register your models here.

class Admin_Penjualan(admin.ModelAdmin):

    list_display = ['kode_penjualan','kode_pemesanan','tanggal_penjualan','total_penjualan']
    search_fields = ['kode_penjualan','kode_pemesanan']
    list_per_page = 15

admin.site.register(Penjualan, Admin_Penjualan)


class Admin_DetailPenjualan(admin.ModelAdmin):

	list_display = ['kode_penjualan','kd_obat','jumlah','total_harga_perobat']
	list_per_page = 15

admin.site.register(DetailPenjualan, Admin_DetailPenjualan)