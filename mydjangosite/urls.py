from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mydjangosite.views.home', name='home'),
    # url(r'^mydjangosite/', include('mydjangosite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),

    url(r'^blog/$', 'blog.views.index'),
    url(r'^blog/details/(?P<id>\d+)/$', 'blog.views.details'),
)
