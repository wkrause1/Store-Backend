# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=400)),
                ('product_description', models.CharField(max_length=600)),
                ('product_price', models.FloatField(default=0.0)),
            ],
        ),
    ]
