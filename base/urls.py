from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('fantasyleague.base.views',
    # Example:
    (r'^teams/', 'teams_list'),
    (r'^players/(?P<position_id>-?\d+)/(?P<team_id>-?\d+)/(?P<value_id>-?\d+)/$', 'players_list'),
    (r'^playerstats/(?P<player_id>\d+)/$', 'player_stats'),
    (r'^player_details/(?P<player_id>\d+)/$', 'player_details'),


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),

)
