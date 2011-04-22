from fantasyleague.base.models import *
from django.contrib import admin
from forms import *

class TeamPlayerInline(admin.TabularInline):
    model = TeamPlayer
    extra = 1
    verbose_name_plural = 'Team Players'

class PlayerTeamInline(admin.TabularInline):
    model = TeamPlayer
    extra = 1
    verbose_name_plural = 'Team(s)'

class PlayerStatsInline(admin.TabularInline):
    model = PlayerStats
    extra = 1
    verbose_name_plural = 'Player Statistics'
    list_display = ('goals',)

class FixtureScorerInline(admin.TabularInline):
    model = FixtureScorer
    extra = 5
    verbose_name_plural = 'Scorers/Assisters'


class FixtureInline(admin.TabularInline):
    model = Fixture
    extra = 10
    verbose_name_plural = 'GameWeek Fixtures'
    inlines = (FixtureScorerInline, )


class TeamAdmin(admin.ModelAdmin):
    inlines = (TeamPlayerInline,)


class PlayerAdmin(admin.ModelAdmin):
    inlines = (PlayerTeamInline, PlayerStatsInline)


class PositionAdmin(admin.ModelAdmin):
    model = Position(Position)


class VenueAdmin(admin.ModelAdmin):
    model = Venue


class FixtureAdmin(admin.ModelAdmin):
    model = Fixture
    inlines = (FixtureScorerInline,)



class GameWeekAdmin(admin.ModelAdmin):
    model = GameWeek
    inlines = (FixtureInline, )


class ValueRangeAdmin(admin.ModelAdmin):
    model = ValueRange



admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Fixture, FixtureAdmin)
admin.site.register(GameWeek, GameWeekAdmin)
admin.site.register(ValueRange, ValueRangeAdmin)