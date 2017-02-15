from django.contrib import admin

from costumer.models import costumer, penjualan_obat, detail_penjualan_obat

# Register your models here.

class admin_costumer(admin.ModelAdmin):

	list_display = ['kd_costumer','nama_costumer','alamat_costumer']
	search_fields = ['kd_costumer','nama_costumer']
	list_per_page = 20

admin.site.register(costumer, admin_costumer)


class admin_penjualan_obat(admin.ModelAdmin):

	list_display = ['kd_penjualan','kd_costumer_obat','tgl_penjualan','total_penjualan']
	list_per_page = 20

admin.site.register(penjualan_obat, admin_penjualan_obat)


class admin_detail_penjualan(admin.ModelAdmin):

	list_display = ['kd_penjualan_detail','kd_obat_detail','jumlah_jual','total_harga_perobat']
	list_per_page = 20

admin.site.register(detail_penjualan_obat, admin_detail_penjualan)