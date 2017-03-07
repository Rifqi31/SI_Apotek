from django.contrib import admin

from Obat.models import Data_Obat


# Register your models here.
class Admin_Data_Obat(admin.ModelAdmin):
    list_display = ['kode_obat','kode_pembelian_suplier','nama_obat', 'jenis_obat', 'bentuk_obat', 'harga_obat', 'stock_obat', 'kode_suplier',
                    'nama_suplier']
    list_filter = ['jenis_obat', 'bentuk_obat']
    search_fields = ['nama_obat', 'kode_obat', 'suplier_obat']
    list_per_page = 15


admin.site.register(Data_Obat, Admin_Data_Obat)
