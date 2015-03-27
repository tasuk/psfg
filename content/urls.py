from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^labs$', views.labs),
    url(r'^mail$', views.mail),
    url(r'^', include('cms.urls')),
)
