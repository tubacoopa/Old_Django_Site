from django.conf.urls import patterns, url

from mysite import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
	url(r'^loggedout/$', views.my_logout, name='logout'),
	url(r'^register/$', views.register_page, name='register'),
	url(r'^registered/$', views.register, name='registered'),
	url(r'^post/$', views.post_page, name='post'),
	url(r'^posted/$', views.post, name='posted'),
	url(r'^follow/$', views.follow_page, name='follow'),
	url(r'^followed/$', views.follow, name='followed'),
)