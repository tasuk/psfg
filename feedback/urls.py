from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^ask/', views.ask, name='ask'),
    url(r'^give/(?P<public_id>[a-zA-Z0-9]+)', views.give, name='give'),
)
