from django.contrib import admin

from Transaksi.models import*
# Register your models here.

class Admin_penjualan(admin.ModelAdmin):
    list_display = ['kode_penjualan', 'nama_pelanggan', 'total_barang', 'total_penjualan']
    seacrch_display = ['kode_penjualalan', 'kode_pemesanan', 'nama_pelanggan']
    list_per_page = 15


admin.site.register(Data_Penjualan, Admin_penjualan)
