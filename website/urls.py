from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^mysite/', include('mysite.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
