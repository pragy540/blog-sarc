# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-05 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default='djangodbmodelsfieldscharfield', max_length=200),
        ),
    ]
