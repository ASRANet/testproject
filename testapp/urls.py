from django.conf.urls import patterns, include, url
from testapp import views

urlpatterns = patterns('',
                       url(r'^/$', views.index))
