# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 12:22
from __future__ import unicode_literals

import ckeditor.fields
import customutils.customfields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('text', ckeditor.fields.RichTextField()),
                ('thumbnail', customutils.customfields.ContentTypeRestrictedFileField(default='', upload_to='thumbnail-photo')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Section'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='posts.Tag'),
        ),
    ]
