from django.contrib import admin

from suplier.models import suplier
# Register your models here.

class admin_suplier(admin.ModelAdmin):

	list_display = ['kd_suplier','nama_suplier','alamat_suplier']
	lis_per_page = 20


admin.site.register(suplier, admin_suplier)