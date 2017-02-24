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
from django.conf.urls import url,include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

# app as view
from Obat import views as obat_view
from Pelanggan import views as pelanggan_view
from Pemesanan import views as pemesanan_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', obat_view.homepage),

    url(r'^obat/', obat_view.Data_Obat),
    url(r'^jenis_obat/', obat_view.Data_JenisObat),

    url(r'^pelanggan/', pelanggan_view.Data_Pelanggan),
    url(r'^pemesanan/', pemesanan_view.Data_Pemesanan),
    url(r'^detail_pemesanan/', pemesanan_view.Data_DetailPemesanan),

]
