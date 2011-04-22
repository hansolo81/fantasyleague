from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('fantasyleague.league.views',
    (r'^leagues/$', 'show_leagues'),
    (r'^league/(?P<league_id>\d+)/$', 'show_league'),
    (r'^join_league/$', 'show_join_league'),
    (r'^create_league/$', 'show_create_league'),
)
