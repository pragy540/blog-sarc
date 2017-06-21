# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post, Section, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	filter_horizontal = ['tags', ]
	list_display = ['author', 'title', 'get_tags']
	# list_filter = ['']
	search_fields = ['tags']

admin.site.register(Post, PostAdmin)
admin.site.register(Section)
admin.site.register(Tag)