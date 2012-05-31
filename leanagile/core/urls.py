from django.conf.urls.defaults import *


urlpatterns = patterns('core.views',
    url(r'^$', view='index', name='index'),
)
