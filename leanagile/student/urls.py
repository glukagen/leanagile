from django.conf.urls.defaults import *


urlpatterns = patterns('student.views',
    url(r'^first/$', view='first', name='student-first'),
    url(r'^last/$', view='last', name='student-last'),
    url(r'^add/$', view='add', name='student-add'),
    url(r'^(?P<id>.*)/edit/$', view='edit', name='student-edit'),
    url(r'^(?P<id>.*)/remove/$', view='delete', name='student-delete'),
    url(r'^(?P<id>.*)/$', view='profile', name='student-profile'),
)
