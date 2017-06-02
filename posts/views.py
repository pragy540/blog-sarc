# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post, Section
from django.db.models import Q


# Create your views here.

def paginator_x(all_posts,request):
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
	return posts

def search_function(string):
	posts_qs = Post.objects.all().filter(Q(tags__tag__icontains = string)|Q(title__icontains = string))
	return posts_qs



def index(request):
	if request.method == "GET":
		all_posts = Post.objects.all()
		posts = paginator_x(all_posts,request)
		return render(request, 'index.html',{'all_posts':posts,'section': -1})
	elif request.method == "POST":
		search_str = request.POST.get("search")
		search_posts = search_function(search_str)
		if not search_posts:
			return render(request, 'search.html',{})
		else:
			return render(request, 'index.html',{'all_posts':search_posts,'section': 0})


def hotc(request):
	if request.method == "GET":
		s = Section.objects.get(section = "History of the Campus")
		all_posts = Post.objects.all().filter(section = s)
		posts = paginator_x(all_posts,request)
		return render(request, 'index.html',{'all_posts':posts,'section': 1})
		
def alumni_research(request):
	if request.method == "GET":
		s = Section.objects.get(section = "Alumni and Research")
		all_posts = Post.objects.all().filter(section = s)
		posts = paginator_x(all_posts,request)
		return render(request, 'index.html',{'all_posts':posts,'section':2})

def prof_interview(request):
	if request.method == "GET":
		s = Section.objects.get(section = "Tete-a-tete with Professors")
		all_posts = Post.objects.all().filter(section = s)
		posts = paginator_x(all_posts,request)
		return render(request, 'index.html',{'all_posts':posts,'section':3})

def kya(request):
	if request.method == "GET":
		s = Section.objects.get(section = "Know Your Alumni")
		all_posts = Post.objects.all().filter(section = s)
		posts = paginator_x(all_posts,request)
		return render(request, 'index.html',{'all_posts':posts,'section':4})


