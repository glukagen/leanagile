from django.conf.urls.defaults import *


urlpatterns = patterns('student.views',
    #url(r'^/$', view='index', name='student-index'),
    url(r'^add/$', view='add', name='student-add'),
)
