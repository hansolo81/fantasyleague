from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('fantasyleague.teammanagement.views',
    # Example:
    (r'^myteam/$', 'show_myteam'),
    (r'^transfers/$', 'show_myteam_transfers'),
    (r'^profile/$', 'show_myteam_profile'),
    (r'^firsttime/$', 'show_firsttime'),


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),

)
