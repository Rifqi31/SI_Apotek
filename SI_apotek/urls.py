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
<<<<<<< HEAD
from Obat import views as obat_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', obat_view.homepage),
    
    url(r'^obat/', obat_view.Data_Obat),
    url(r'^jenis_obat/', obat_view.Data_JenisObat),

=======
from costumer import views as costumer_view
from suplier import views as suplier_view
from obat import views as obat_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', costumer_view.homepage),

    url(r'^costumer/', costumer_view.data_costumer),

    url(r'^penjualan/', costumer_view.data_penjualan_obat),
    url(r'^penjualan_detail/', costumer_view.data_penjualan_obat_detail),
  

    url(r'^suplier/', suplier_view.data_suplier),

    url(r'^pembelian/', suplier_view.data_pembelian_obat),
    url(r'^pembelian_detail/', suplier_view.data_pembelian_obat_detail),


    url(r'^obat/', obat_view.data_obat),
>>>>>>> d6d284c31af1d237ce63e0dced0cc56b014c14a1
]
