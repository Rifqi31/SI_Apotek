from django.contrib import admin

from Pemesanan.models import Data_Pemesanan, DetailPemesanan


# Register your models here.
class Admin_Pemesanan(admin.ModelAdmin):
    list_display = ['kode_pemesanan', 'tanggal_pemesanan', 'kode_pelanggan', 'nama_pelanggan', 'karyawan']
    search_fields = ['kode_pemesanan', 'karyawan', 'nama_pelanggan']
    list_per_page = 15


admin.site.register(Data_Pemesanan, Admin_Pemesanan)


class Admin_DetailPemesanan(admin.ModelAdmin):
    list_display = ['kode_pemesanan', 'nama_pemesan', 'kode_obat', 'nama_obat', 'kode_resep', 'jumlah',
                    'total_harga_perobat']
    search_fields = ['kode_pemesanan', 'nama_pemesan', 'kode_obat', 'kode_resep']
    list_per_page = 15


admin.site.register(DetailPemesanan, Admin_DetailPemesanan)
