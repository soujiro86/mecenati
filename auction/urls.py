from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import AuctionListView

urlpatterns = patterns('',
    url(r'^list/$', AuctionListView.as_view(), name='auction-list'),

)

