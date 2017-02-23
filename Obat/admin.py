from django.contrib import admin

from Obat.models import*

# Register your models here.

class Admin_Obat(admin.ModelAdmin):

	list_display = ['kode_obat','nama_obat','kode_jenis_obat','harga_obat','stock_obat']
	list_filter = ['kode_jenis_obat','stock_obat']
	search_fields = ['nama_obat','kode_obat','kode_jenis_obat']
	list_per_page = 15


admin.site.register(Obat, Admin_Obat)


class Admin_JenisObat(admin.ModelAdmin):

	list_display = ['kode_jenis_obat','nama_jenis_obat']
	list_filter = ['nama_jenis_obat']
	search_fields = ['kode_jenis_obat']
	list_per_page = 15


admin.site.register(JenisObat, Admin_JenisObat)