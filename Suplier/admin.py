from django.contrib import admin

from Suplier.models import*

# Register your models here.

class Admin_Suplier(admin.ModelAdmin):

	list_display = ['kode_suplier','nama_suplier','alamat_suplier','telepon_suplier','email_suplier']
	search_fields = ['kode_suplier','nama_suplier','telepon_suplier','email_suplier']
	list_per_page = 15

admin.site.register(Suplier, Admin_Suplier)