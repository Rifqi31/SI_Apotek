from django.contrib import admin

from Suplier.models import Data_Suplier

# Register your models here.

class Admin_Data_Suplier(admin.ModelAdmin):

	list_display = ['kode_suplier','nama_suplier','alamat_suplier','telepon_suplier','email_suplier']
	search_fields = ['kode_suplier','nama_suplier','telepon_suplier','email_suplier']
	list_per_page = 15

admin.site.register(Data_Suplier, Admin_Data_Suplier)