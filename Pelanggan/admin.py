from django.contrib import admin

from Pelanggan.models import*

# Register your models here.

class Admin_Pelanggan(admin.ModelAdmin):

	list_display = ['kode_pelanggan','nama_pelanggan','alamat_pelanggan','nomer_telepon',]
	search_fields = ['kode_pelanggan','nama_pelanggan','nomer_telepon']
	list_per_page = 15


admin.site.register(Pelanggan, Admin_Pelanggan)