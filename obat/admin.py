from django.contrib import admin

from obat.models import obat

# Register your models here.

class admin_obat(admin.ModelAdmin):

	list_display = ['kd_obat','nama_obat','tipe_obat','harga_jual']
	list_filter = ['tipe_obat']
	search_fields = ['nama_obat','kd_obat']
	list_per_page = 20


admin.site.register(obat, admin_obat)