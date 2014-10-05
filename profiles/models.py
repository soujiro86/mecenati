from django.db import models
from django.contrib.auth.models import User


class Portfolio(models.Model):
    owner = models.ForeignKey(User, related_name='portfolio_set')
    image = models.ImageField()
    description = models.TextField()


class Skill(models.Model):
    name = models.CharField(max_length=500)


class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile_set')
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    portrait = models.ImageField()
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=400)
    district = models.CharField(max_length=400)  # "provincia" in english
    country = models.CharField(max_length=400)
    artist = models.BooleanField(default=False)
    patron = models.BooleanField(default=False)
    skill_set = models.ManyToManyField(Skill, related_name='skilled_profile_set', null=True)

