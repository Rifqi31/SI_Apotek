# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 05:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suplier',
            fields=[
                ('kode_suplier', models.CharField(max_length=5, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{1,5}$')])),
                ('nama_suplier', models.CharField(max_length=50)),
                ('alamat_suplier', models.TextField(validators=[django.core.validators.MaxLengthValidator(100)])),
                ('telepon_suplier', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')])),
                ('email_suplier', models.EmailField(max_length=254)),
            ],
        ),
    ]
