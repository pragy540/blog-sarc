# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post, Section


# Create your views here.

def index(request):
	if request.method == "GET":
		all_posts = Post.objects.all()
		paginator = Paginator(all_posts,2)
		page = request.GET.get('page')
		try:
			posts = paginator.page(page)
		except PageNotAnInteger:
		# If page is not an integer, deliver first page.
			posts = paginator.page(1)
		except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
			posts = paginator.page(paginator.num_pages)
	return render(request, 'index.html',{'all_posts':posts,'section':'secction0'})

def hotc(request):
	if request.method == "GET":
		s = Section.objects.get(section = "History of the Campus")
		all_posts = Post.objects.all().filter(section = s)
		return render(request, 'index.html',{'all_posts':all_posts,'section': 1})
		
def alumni_research(request):
	if request.method == "GET":
		s = Section.objects.get(section = "Alumni and Research")
		all_posts = Post.objects.all().filter(section = s)
		return render(request, 'index.html',{'all_posts':all_posts,'section':2})

def prof_interview(request):
	if request.method == "GET":
		s = Section.objects.get(section = "Tete-a-tete with Professors")
		all_posts = Post.objects.all().filter(section = s)
		return render(request, 'index.html',{'all_posts':all_posts,'section':3})

def kya(request):
	if request.method == "GET":
		s = Section.objects.get(section = "Know Your Alumni")
		all_posts = Post.objects.all().filter(section = s)
		return render(request, 'index.html',{'all_posts':all_posts,'section':4})
