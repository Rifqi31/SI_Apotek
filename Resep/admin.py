from django.contrib import admin

from Resep.models import*

# Register your models here.

class Admin_Resep(admin.ModelAdmin):

	list_display = ['kode_resep','tanggal_resep','nama_pasien']
	search_fields = ['kode_resep','nama_pasien']
	list_per_page = 15

admin.site.register(Resep, Admin_Resep)