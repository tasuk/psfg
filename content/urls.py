from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^mail/$', views.mail),
    url(r'^meetup/$', views.meetup),
    url(r'^', include('cms.urls')),
)
