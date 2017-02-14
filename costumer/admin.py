from django.contrib import admin

from costumer.models import costumer

# Register your models here.

class admin_costumer(admin.ModelAdmin):

	list_display = ['kd_costumer','nama_costumer','alamat_costumer']
	search_fields = ['kd_costumer','nama_costumer']
	list_per_page = 20

admin.site.register(costumer, admin_costumer)

