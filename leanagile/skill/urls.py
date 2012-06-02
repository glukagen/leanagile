from django.conf.urls.defaults import *


urlpatterns = patterns('skill.views',
    #url(r'^set_status/$', view='set_status', name='set-skill-status'),
    url(r'^change_status/(?P<status_id>.*)/$', view='change_status', name='change-skill-status'),
)
