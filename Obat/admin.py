from django.contrib import admin

from Obat.models import Data_Obat, Data_Resep


# Register your models here.
class Admin_Data_Obat(admin.ModelAdmin):
    list_display = ['kode_obat','kode_pembelian_suplier','nama_obat', 'jenis_obat', 'bentuk_obat', 'harga_obat', 'stock_obat', 'kode_suplier',
                    'nama_suplier']
    list_filter = ['jenis_obat', 'bentuk_obat']
    search_fields = ['nama_obat', 'kode_obat', 'suplier_obat']
    list_per_page = 15


admin.site.register(Data_Obat, Admin_Data_Obat)


class Admin_Resep(admin.ModelAdmin):
    list_display = ['kode_resep', 'tanggal_resep', 'nama_pasien']
    search_fields = ['kode_resep', 'nama_pasien']
    list_per_page = 15


admin.site.register(Data_Resep, Admin_Resep)
