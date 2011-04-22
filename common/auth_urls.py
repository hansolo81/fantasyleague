from django.conf.urls.defaults import *

urlpatterns = patterns('django.contrib.auth.views',
                       (r'^login/$', 'login', {'template_name': 'common/login.html'}),
                       (r'^logout/$', 'logout_then_login'),
                       )
