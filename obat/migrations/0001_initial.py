# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='obat',
            fields=[
                ('kd_obat', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_obat', models.CharField(max_length=15)),
                ('tipe_obat', models.CharField(max_length=15)),
                ('harga_jual', models.IntegerField()),
            ],
        ),
    ]
