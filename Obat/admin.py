from django.contrib import admin

from Obat.models import Data_Pembelian, Data_Obat, Data_Resep


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


class Admin_Data_Obat(admin.ModelAdmin):
    list_display = ['kode_obat','nama_obat','jenis_obat', 'bentuk_obat', 'harga_obat', 'stock_obat','nama_suplier']
    list_filter = ['jenis_obat', 'bentuk_obat']
    search_fields = ['nama_obat', 'kode_obat', 'suplier_obat']
    list_per_page = 15


admin.site.register(Data_Obat, Admin_Data_Obat)


class Admin_Resep(admin.ModelAdmin):
    list_display = ['kode_resep', 'tanggal_resep', 'nama_pasien']
    search_fields = ['kode_resep', 'nama_pasien']
    list_per_page = 15


admin.site.register(Data_Resep, Admin_Resep)
