from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'homepage.views.index'),
    url(r'^labs$', 'homepage.views.labs'),
    url(r'^mail$', 'homepage.views.mail'),
    url(r'^feedback', 'feedback.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
