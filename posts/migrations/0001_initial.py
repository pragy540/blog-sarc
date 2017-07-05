# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-05 09:33
from __future__ import unicode_literals

import ckeditor_uploader.fields
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
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('thumbnail', customutils.customfields.ContentTypeRestrictedFileField(default='', upload_to='thumbnail-photo')),
                ('likes', models.PositiveIntegerField(blank=True, default=0)),
                ('readtime', models.PositiveIntegerField(default=3)),
                ('slug', models.SlugField(blank=True, default='', max_length=200)),
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
