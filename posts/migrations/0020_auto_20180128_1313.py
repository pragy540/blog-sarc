# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-28 13:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='from_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='body',
            new_name='message',
        ),
    ]