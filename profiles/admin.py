from django.contrib import admin
from .models import Portfolio, Profile, Skill
from django.contrib.auth.models import User


class PortfolioAdmin(admin.ModelAdmin):
    model = Portfolio


class SkillAdmin(admin.ModelAdmin):
    model = Skill


    
admin.site.register(Portfolio, PortfolioAdmin,)
admin.site.register(Skill, SkillAdmin,)
