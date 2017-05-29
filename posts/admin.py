# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post, Section, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Section)
admin.site.register(Tag)