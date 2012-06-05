from django.conf.urls.defaults import *


urlpatterns = patterns('skill.views',
    url(r'^change_status/(?P<status_id>.*)/$',
        view='change_status', name='change-skill-status'),
    url(r'^change_progress_status/(?P<status_id>.*)/$',
        view='change_progress_status', name='change-progress-status'),
)
