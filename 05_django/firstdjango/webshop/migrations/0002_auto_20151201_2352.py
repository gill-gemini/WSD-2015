# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.CharField(max_length=23, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(max_length=23, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='datebirth',
            field=models.CharField(max_length=23, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=23, blank=True),
        ),
    ]
