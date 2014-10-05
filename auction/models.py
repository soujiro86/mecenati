from django.db import models
from django.contrib.auth.models import User
from profiles.models import Skill


class Auction(models.Model):
    """
    the wall that need to be "artistified"
    """

    title = models.CharField(max_length=400)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='auction_set')
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.IntegerField()
    length = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField(auto_now=True)
    requirements = models.ManyToManyField(Skill, related_name="auction_requirements_set")

    # Geolocalization
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=400)
    district = models.CharField(max_length=400)  # "provincia" in english
    country = models.CharField(max_length=400)


class Bid(models.Model):
    """
    the offers maded by the artists
    """
    bidder = models.ForeignKey(User, related_name='bid_set')
    title = models.CharField(max_length=400)
    description = models.TextField()
    draft = models.ImageField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_time = models.IntegerField()  # number of days
    chosen = models.BooleanField(default=False)


class Milestone(models.Model):
    """
    the milestones for the artist works
    """
    auction = models.ForeignKey(Auction, related_name='milestone_set')
    description = models.TextField()
    estimated_time = models.IntegerField()  # number of days
    checked = models.BooleanField(default=False)


class Feedback(models.Model):
    """
    The feedback for a single work
    """
    bid = models.OneToOneField(Bid, related_name='feedback_set')
    rating = models.IntegerField()




