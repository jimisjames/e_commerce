# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-25 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20180925_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='name',
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default='poop', upload_to='../apps/store/static/store/pics'),
            preserve_default=False,
        ),
    ]
