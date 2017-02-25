# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 08:32
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Obat', '0001_initial'),
        ('Penjualan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailPenjualan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.IntegerField()),
                ('total_harga_perobat_currency', djmoney.models.fields.CurrencyField(choices=[(b'IDR', b'Rupiah'), (b'USD', 'US Dollar')], default='IDR', editable=False, max_length=3)),
                ('total_harga_perobat', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), default_currency=b'IDR', max_digits=10)),
                ('kd_obat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Obat.Obat')),
            ],
        ),
        migrations.AddField(
            model_name='penjualan',
            name='total_penjualan',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), default_currency=b'IDR', max_digits=10),
        ),
        migrations.AddField(
            model_name='penjualan',
            name='total_penjualan_currency',
            field=djmoney.models.fields.CurrencyField(choices=[(b'IDR', b'Rupiah'), (b'USD', 'US Dollar')], default=b'IDR', editable=False, max_length=3),
        ),
        migrations.AddField(
            model_name='detailpenjualan',
            name='kode_penjualan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Penjualan.Penjualan'),
        ),
    ]
