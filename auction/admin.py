from django.contrib import admin
from .models import Auction


class AuctionAdmin(admin.ModelAdmin):
    model = Auction


    
admin.site.register(Auction,AuctionAdmin,)
