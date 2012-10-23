from django.conf.urls.defaults import *


urlpatterns = patterns('domaintools.views',
    url(r'^update/(?P<domain>[a-z0-9-.]+)/', 'dynamic_dns_update'),
    url(r'^read/(?P<domain>[a-z0-9-.]+)/', 'dynamic_dns_read'),
)
