# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-25 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20180925_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_ids',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(related_name='carts', to='store.Product'),
        ),
    ]
