# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Post, Stats, Message
from .forms import ContactForm
from django.db.models import Q

from django.template.defaultfilters import slugify

# Create your views here.

def paginator_x(all_posts,request):
	paginator = Paginator(all_posts,1)
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
	posts_qs = Post.objects.all().filter(published = True).filter(Q(tags__tag__icontains = string)|Q(title__icontains = string)|Q(author__icontains = string)).distinct()
	return posts_qs

def index(request):
	if request.method == "GET":
		all_posts = Post.objects.all().filter(published = True)
		number = Stats.objects.get(name='sarcadmin')
		number.hits +=1
		number.save()
		#all_posts = paginator_x(all_posts,request)
		return render(request, 'index.html',{'all_posts':all_posts,'filter': 'Latest'})
	elif request.method == "POST":
		search_str = request.POST.get("search")
		search_posts = search_function(search_str)
		if not search_posts:
			return render(request, 'search.html',{})
		else:
			return render(request, 'index.html',{'all_posts':search_posts,'filter': 'Latest'})

def popular(request):
	if request.method == "GET":
		all_posts = Post.objects.all().order_by('-views').filter(published = True)
		#all_posts = paginator_x(all_posts,request)
		return render(request, 'index.html',{'all_posts':all_posts,'filter':'Popular'})

def preview(request):
	if request.method == "GET":
		all_posts = Post.objects.all().filter(published = False)
		#all_posts = paginator_x(all_posts,request)
		return render(request, 'index.html',{'all_posts':all_posts,'filter':'Latest'})

def old(request):
	if request.method == "GET":
		all_posts = Post.objects.all().filter(published = True).reverse()
		#all_posts = paginator_x(all_posts,request)
		return render(request, 'index.html',{'all_posts':all_posts,'filter':'Oldest'})

def post(request, url):
	post = Post.objects.get(slug = slugify(url))
	post.views +=1
	post.save()
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		message = Message()
		if form.is_valid():
			data = form.save(commit=False)
			data.save()
			subject = "SARC BLOG| " + data.subject
			from_email = data.email
			body = data.message
			try:
				send_mail(subject, body, from_email, ['mrinal.dharmik@gmail.com','mantrikaran@gmail.com','tanaytirpude123@gmail.com'], fail_silently=False)
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			messages.success(request, "Message recieved. \nWe will get back to you as soon as possible.")
	return render(request, 'post.html', {'post':post,'form':form})

#
def hits(request):
	number = Stats.objects.get(name='sarcadmin')
	all_posts = Post.objects.all().filter(published = True)
	return render(request, 'hits.html', {'number':number,'all_posts':all_posts})


