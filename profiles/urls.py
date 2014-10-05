from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import ArtistDetailView, ArtistListView

urlpatterns = patterns('',
    url(r'^list/$', ArtistListView.as_view(), name='artist-list'),
    url(r'^detail/(?P<pk>[\d]+)/$', ArtistDetailView.as_view(), name='artist-detail'),

)

