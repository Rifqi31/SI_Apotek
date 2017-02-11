from django.contrib import admin

from penjualan.models import penjualan_obat, detail_penjualan

# Register your models here.

class admin_penjualan_obat(admin.ModelAdmin):

	list_display = ['kd_penjualan','kd_costumer_obat','tgl_penjualan','total_penjualan']
	search_fields = ['kd_penjualan','kd_costumer_obat']
	list_per_page = 20

admin.site.register(penjualan_obat, admin_penjualan_obat)


class admin_detail_penjualan(admin.ModelAdmin):

	list_display = ['kd_penjualan_detail','kd_obat_detail','jumlah_jual','total_harga_perobat']
	search_fields = ['kd_penjualan_detail','kd_obat_detail']
	list_per_page = 20

admin.site.register(detail_penjualan, admin_detail_penjualan)