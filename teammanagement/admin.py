from fantasyleague.base.models import *
from django.contrib import admin
from forms import *

class MyTeamPlayerInline(admin.TabularInline):
    model = MyTeamPlayer
    extra = 1
    verbose_name_plural = 'Team Players'

class MyTeamAdmin(admin.ModelAdmin):
    inlines = (MyTeamPlayerInline,)



admin.site.register(MyTeam, MyTeamAdmin)