from fantasyleague.base.models import *
from fantasyleague.league.models import *
from django.contrib import admin

class LeagueTeamInline(admin.TabularInline):
    model = LeagueTeam
    extra = 1
    verbose_name_plural = 'League Teams'

class LeagueAdmin(admin.ModelAdmin):
    inlines = (LeagueTeamInline,)



admin.site.register(League, LeagueAdmin)