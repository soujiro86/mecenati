from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView



urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('profiles.urls')),
    url(r'^contests/', include('auction.urls')),
    url(r'^$', TemplateView.as_view(template_name="mecenati/home.html")),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$',
         'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
         })
    )

