from django.contrib import admin

from Costumer.models import*

# Register your models here.
class Admin_Pelanggan(admin.ModelAdmin):
    list_display = ['kode_pelanggan', 'nama_pelanggan', 'alamat_pelanggan', 'nomer_telepon', ]
    search_fields = ['nama_pelanggan', 'nomer_telepon']
    list_per_page = 15


admin.site.register(Data_Pelanggan, Admin_Pelanggan)

class Admin_Pemesanan(admin.ModelAdmin):
    list_display = ['kode_pemesanan', 'tanggal_pemesanan', 'pelanggan', 'karyawan']
    search_fields = ['kode_pemesanan', 'karyawan', 'pelanggan']
    list_per_page = 15


admin.site.register(Data_Pemesanan, Admin_Pemesanan)


class Admin_DetailPemesanan(admin.ModelAdmin):
    list_display = ['nama_pemesan', 'nama_obat', 'kode_resep', 'jumlah',
                    'total_harga_perobat']
    search_fields = ['nama_pemesan', 'nama_obat','kode_obat', 'kode_resep']
    list_per_page = 15


admin.site.register(DetailPemesanan, Admin_DetailPemesanan)
