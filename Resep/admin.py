from django.contrib import admin

from Resep.models import Data_Resep

# Register your models here.

class Admin_Resep(admin.ModelAdmin):

	list_display = ['kode_resep','tanggal_resep','kode_pelanggan','nama_pasien']
	search_fields = ['kode_resep','nama_pasien']
	list_per_page = 15

admin.site.register(Data_Resep, Admin_Resep)