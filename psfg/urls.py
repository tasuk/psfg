from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'homepage.views.index'),
    url(r'^labs$', 'homepage.views.labs'),
    url(r'^mail$', 'homepage.views.mail'),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
