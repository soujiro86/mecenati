from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from .models import Profile


class ArtistListView(ListView):
    template_name = "profiles/artist_list.html"
    model = User

    def get_queryset(self):
        queryset = super(ArtistListView, self).get_queryset()
        queryset = queryset.filter(profile_set__artist=True)
        return queryset


class ArtistDetailView(DetailView):
    template_name = "profiles/artist_detail.html"
    model = User




