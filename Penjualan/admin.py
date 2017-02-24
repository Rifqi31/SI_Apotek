from django.contrib import admin

from Penjualan.models import*
# Register your models here.

class Admin_Penjualan(admin.ModelAdmin):

    list_display = ['kode_penjualan','kode_pemesanan','tanggal_penjualan']
    search_fields = ['kode_penjualan','kode_pemesanan']
    list_per_page = 15

admin.site.register(Penjualan, Admin_Penjualan)
