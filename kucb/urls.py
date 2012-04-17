from django.conf.urls.defaults import patterns, include, url
from django.views.decorators.cache import cache_page
import news.views
import community.views
import about.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kucb.views.home', name='home'),
    # url(r'^kucb/', include('kucb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^news/$', news.views.news),

    url(r'^sitemap\.xml', news.views.sitemap),
    url(r'^rss/', news.views.rss),
    url(r'^news/article/(?P<slug>[a-z0-9\-]+)/$', news.views.article),
    url(r'^post/(?P<slug>[a-z0-9\-]+)/$', news.views.post),

    url(r'^news/category/(?P<slug>[a-z0-9\-]+)/$', news.views.category),
    url(r'^$', news.views.index),
    url(r'^community/$', community.views.community),
    url(r'^community/events/$', community.views.events),
    url(r'^community/classifieds/$', community.views.classifieds),
    url(r'^community/add/event/$', community.views.add_event),
    url(r'^community/events/(?P<slug>[a-z0-9\-]+)/$', community.views.event),
    url(r'^community/blotter/$', community.views.blotter),
    url(r'^about/$', about.views.about),
    url(r'^about/profile/(\d+)/$', about.views.profile),
    url(r'^blotter/upload/$', community.views.upload_blotter),
    url(r'^admin/', include(admin.site.urls)),
)
