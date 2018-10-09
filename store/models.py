# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=400)
    product_description = models.CharField(max_length=600)
    product_price = models.FloatField(default=0.0)
    product_image = models.URLField()

    def __str__(self):
        return self.product_name