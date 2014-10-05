from django.contrib import admin
from .models import Portfolio, Profile, Skill
from django.contrib.auth.models import User


class ProfileAdmin(admin.ModelAdmin):
    model = Profile

class PortfolioAdmin(admin.ModelAdmin):
    model = Portfolio


class SkillAdmin(admin.ModelAdmin):
    model = Skill


    
admin.site.register(Portfolio, PortfolioAdmin,)
admin.site.register(Profile, ProfileAdmin,)
admin.site.register(Skill, SkillAdmin,)
