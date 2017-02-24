# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 07:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resep',
            fields=[
                ('kode_resep', models.CharField(max_length=5, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('tanggal_resep', models.DateField()),
                ('nama_pasien', models.CharField(max_length=50)),
            ],
        ),
    ]
