from django.contrib import admin

from suplier.models import suplier, pembelian_obat

# Register your models here.

class admin_suplier(admin.ModelAdmin):

	list_display = ['kd_suplier','nama_suplier','alamat_suplier']
	lis_per_page = 20


admin.site.register(suplier, admin_suplier)

class pembelian_obat_admin(admin.ModelAdmin):

	list_display = ['kd_pembelian','kd_suplier_obat','tgl_pembelian','total_pembelian']
	list_per_page = 20

admin.site.register(pembelian_obat, pembelian_obat_admin)	

