from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from mysite.models import Post, Follow, ImageUploadForm
import datetime
from django.db import IntegrityError, DataError

def index(request):
	if request.user.is_authenticated():
		remove = Post.objects.filter(expiration__lt=timezone.now())
		remove.delete()
		a = Follow.objects.filter(username=request.user.username)
		b = Post.objects.order_by('expiration')
		return render(request, 'index.html', {'follows':a, 'posts':b})
	else:
		return render(request, 'loggedout.html')
		
def my_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def register_page(request):
	return render(request, 'register.html')
	
def register(request):
	username = request.POST.get('username', 'empty')
	password = request.POST.get('password', 'empty')
	email = request.POST.get('email', 'empty')
	try:
		user = User.objects.create_user(username, email, password)
		user.save()
	except(IntegrityError):
		return render(request, 'register.html', {
            'error_message': "Username taken!"})
	else:
		user = authenticate(username=username, password=password)
		follow = Follow(username=username, following=username)
		follow.save()
		login(request, user)
		return HttpResponseRedirect(reverse('index'))
	
def post_page(request):
	return render(request, 'post.html')
	
def post(request):
	form = ImageUploadForm(request.POST, request.FILES)
	username = request.user.username
	if form.is_valid():
		photo = form.cleaned_data['photo']
	else:
		photo = 'empty'
	text = request.POST.get('text', 'empty')
	expiration = request.POST.get('expiration', 'empty')
	post = Post(username=username, photo=photo, text=text, expiration=expiration)
	try:
		post.save()
	except(DataError):
		return render(request, 'post.html', {
            'error_message': "Posts must be 400 characters or less!"})
	else:
		return HttpResponseRedirect(reverse('index'))
	
def follow_page(request):
	return render(request, 'follow.html')
	
def follow(request):
	username = request.user.username
	following = request.POST.get('following', 'empty')
	try: 
		User.objects.get(username__exact=following)
	except (KeyError, User.DoesNotExist):
		return render(request, 'follow.html', {
            'error_message': "Not a valid user!"})
	else:
		follow = Follow(username=username, following=following)
		follow.save()
		return HttpResponseRedirect(reverse('index'))
