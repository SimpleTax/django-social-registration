from django.conf import settings
from django.conf.urls.defaults import *
from socialregistration.contrib.sapo.views import SapoRedirect, \
    SapoCallback, SapoSetup


urlpatterns = patterns('',
    url('^redirect/$', SapoRedirect.as_view(), name='redirect'),
    url('^callback/$', SapoCallback.as_view(), name='callback'),
    url('^setup/$', SapoSetup.as_view(), name='setup'),
)
