# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('code', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('capital', models.CharField(max_length=255)),
                ('code', models.CharField(unique=True, max_length=255)),
                ('population', models.PositiveIntegerField()),
                ('area', models.PositiveIntegerField()),
                ('continent', models.ForeignKey(to='countrydata.Continent', related_name='countries')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
