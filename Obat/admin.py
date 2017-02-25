from django.contrib import admin

from Obat.models import*

# Register your models here.

class Admin_Obat(admin.ModelAdmin):

	list_display = ['kode_obat','nama_obat','jenis_obat','bentuk_obat','harga_obat','stock_obat']
	list_filter = ['jenis_obat','bentuk_obat']
	search_fields = ['nama_obat','kode_obat','jenis_obat']
	list_per_page = 15


admin.site.register(Obat, Admin_Obat)