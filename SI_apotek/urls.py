"""SI_apotek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# app as view
from Karyawan import views as karyawan_view
from Obat import views as obat_view
from Costumer import views as costumer_view
from Transaksi import views as transaksi_view
from Suplier import views as suplier_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', obat_view.homepage),

    # karyawan
    url(r'^login_karyawan/', karyawan_view.login_karyawan_view),
    url(r'^logout_karyawan/', karyawan_view.logout_karyawan_view),
    url(r'^register_karyawan/', karyawan_view.register_karyawan),
    url(r'^izin_karyawan/', karyawan_view.pengajuan_izin_karyawan),
    url(r'^daftar_izin_karyawan/', karyawan_view.daftar_izin_karyawan),

    url(r'^absen_karyawan/', karyawan_view.absen_karyawan),

    url(r'^daftar_hadir/$', karyawan_view.daftar_hadir_karyawan),
    url(r'^daftar_hadir/cetak/(?P<bulan>\d+)/(?P<tahun>\d+)$', karyawan_view.cetak_absensi, name='show_pdf'),
    # url(r'^daftar_hadir/grafik/(?P<bulan>\d+)/(?P<tahun>\d+)$',karyawan_view.tampil_grafik, name ='show_grafik'),



    # Obat,Resep dan Suplier
    url(r'^obat/', obat_view.isi_data_obat),
    url(r'^daftar_obat/', obat_view.tampil_daftar_obat),
    url(r'^resep/', obat_view.isi_data_resep),
    
    url(r'^suplier/', suplier_view.isi_data_suplier),
    url(r'^daftar_suplier/', suplier_view.tampil_daftar_suplier),

    # Pelanggan dan Pemesanan
    url(r'^pelanggan/', costumer_view.isi_data_pelanggan),
    url(r'^pemesanan/', costumer_view.isi_data_pemesanan),
    url(r'^detail_pemesanan/', costumer_view.data_detailpemesanan),

    # Penjualan dan Pembelian
    url(r'^penjualan/', transaksi_view.hitung_penjualan),
    url(r'^pembelian/', transaksi_view.isi_data_pembelian)
]
