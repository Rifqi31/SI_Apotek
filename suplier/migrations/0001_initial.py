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
            name='suplier',
            fields=[
                ('kd_suplier', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_suplier', models.CharField(max_length=15)),
                ('alamat_suplier', models.TextField()),
            ],
        ),
    ]
