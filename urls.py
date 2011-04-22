from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^base/', include('fantasyleague.base.urls')),
    (r'^teammanagement/', include('fantasyleague.teammanagement.urls')),
    (r'^league/', include('fantasyleague.league.urls')),
    (r'^', include('fantasyleague.common.auth_urls')),
    (r'^accounts/', include('registration.urls')),
    (r'^log_me_in/$', 'fantasyleague.common.views.log_me_in'),


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^sitemedia/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'./sitemedia/', 'show_indexes': True}),
)
