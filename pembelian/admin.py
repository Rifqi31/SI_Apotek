from django.contrib import admin

from pembelian.models import pembelian_obat, detail_pembelian

# Register your models here.

class admin_pembelian_obat(admin.ModelAdmin):

	list_display = ['kd_pembelian','kd_suplier_obat','tgl_pembelian','total_pembelian']
	search_fields = ['kd_pembelian','kd_suplier_obat']
	list_per_page = 20

admin.site.register(pembelian_obat, admin_pembelian_obat)



class admin_detail_pembelian(admin.ModelAdmin):

	list_display = ['kd_pembelian_detail','kd_obat_detail','jumlah_beli','total_harga_perobat']
	search_fields = ['kd_pembelian_detail','kd_obat_detail']
	list_per_page = 20

admin.site.register(detail_pembelian, admin_detail_pembelian)