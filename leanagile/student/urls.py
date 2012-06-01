from django.conf.urls.defaults import *


urlpatterns = patterns('student.views',
    url(r'^add/$', view='add', name='student-add'),
    url(r'^(?P<id>.*)/$', view='profile', name='student-profile'),
)
