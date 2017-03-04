from django.contrib import admin

from Pelanggan.models import Data_Pelanggan

# Register your models here.

class Admin_Pelanggan(admin.ModelAdmin):

	list_display = ['kode_pelanggan','nama_pelanggan','alamat_pelanggan','nomer_telepon',]
	search_fields = ['nama_pelanggan','nomer_telepon']
	list_per_page = 15


admin.site.register(Data_Pelanggan, Admin_Pelanggan)