"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class HomeSitemap(Sitemap):

    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)


class PrioritySitemap(Sitemap):

    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['contactus', 'register', 'uploadAbstract']

    def location(self, item):
        return reverse(item)


class Sitemaps(Sitemap):

    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['venue', 'accomodation', 'travel', 'cookies']

    def location(self, item):
        return reverse(item)

sitemaps = {
    'homepage': HomeSitemap,
    'priority': PrioritySitemap,
    'static': Sitemaps,
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'testapp.views.index', name='index'),
    url(r'^register/', include('register.urls')),
    url(r'^uploadAbstract/', include('uploadAbstract.urls')),
    url(r'^venue/', 'testapp.views.venue', name='venue'),
    url(r'^accomodation/', 'testapp.views.accomodation', name='accomodation'),
    url(r'^contactus/', 'testapp.views.contactus', name='contactus'),
    url(r'^authorinstructions/', 'testapp.views.author_instructions', name='authorInstructions'),
    url(r'^travel/', 'testapp.views.travel', name='travel'),
    url(r'^cookies/', 'testapp.views.cookies', name='cookies'),
    url(r'^$', 'testapp.views.index', name='index'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap'),
                       ]

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )


