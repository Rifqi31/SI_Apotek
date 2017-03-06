from django.contrib import admin

from Pembelian.models import Data_Pembelian

# Register your models here.

class Admin_Pembelian(admin.ModelAdmin):

	list_display = [
		'kode_pembelian',
		'kode_suplier',
		'nama_suplier',
		'kode_obat',
		'nama_obat',
		'tgl_pembelian',
		'total_barang',
		'total_pembelian']
	
	search_fields = ['kode_pembelian','kode_suplier','nama_suplier','kode_obat','nama_obat']
	list_per_page = 15

admin.site.register(Data_Pembelian, Admin_Pembelian)