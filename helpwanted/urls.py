from django.conf.urls.defaults import *
from helpwanted.feeds import OpenPositionsFeed

urlpatterns = patterns('helpwanted.views',
    url(r'^(?P<object_id>\d+)/', 'joblisting_detail', name="job_detail"),
    url(r'^$', 'joblisting_list', name="job_list"),
)

urlpatterns += patterns('',
    url(r'^rss/$', OpenPositionsFeed(), name="job_feed"),
)