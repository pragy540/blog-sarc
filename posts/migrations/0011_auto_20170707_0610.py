# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-07 06:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20170707_0608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date', '-id']},
        ),
    ]
