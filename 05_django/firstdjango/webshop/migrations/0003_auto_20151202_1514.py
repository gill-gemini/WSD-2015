# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0002_auto_20151201_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='city',
        ),
        migrations.RemoveField(
            model_name='product',
            name='country',
        ),
        migrations.RemoveField(
            model_name='product',
            name='datebirth',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.ImageField(null=True, blank=True, max_length=23, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.BigIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
