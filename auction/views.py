from django.views.generic import ListView
from .models import Auction

class AuctionListView(ListView):
    template_name = "auction/auction_list.html"
    model = Auction





