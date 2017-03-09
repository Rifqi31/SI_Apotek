from django.contrib import admin

from Transaksi.models import*
# Register your models here.

class Admin_Pembelian(admin.ModelAdmin):
    list_display = [
        'kode_pembelian',
        #'kode_suplier',
        'nama_suplier',
        'nama_obat',
        'tgl_pembelian',
        'harga_beli',
        'total_barang',
        'total_pembelian']

    search_fields = ['kode_pembelian', 'kode_suplier', 'nama_suplier', 'nama_obat']
    list_per_page = 15


admin.site.register(Data_Pembelian, Admin_Pembelian)


class Admin_penjualan(admin.ModelAdmin):
    list_display = ['kode_penjualan', 'nama_pelanggan', 'total_barang', 'total_penjualan']
    seacrch_display = ['kode_penjualalan', 'kode_pemesanan', 'nama_pelanggan']
    list_per_page = 15


admin.site.register(Data_Penjualan, Admin_penjualan)
