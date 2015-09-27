"""
Main URL Configuration 
"""

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView


urlpatterns = [
    # In production these should be served directly by http server
    url(r'^favicon\.png[/]?$', RedirectView.as_view(url='{}images/favicon.png'.format(settings.STATIC_URL))),
    url(r'^favicon\.ico[/]?$', RedirectView.as_view(url='{}images/favicon.png'.format(settings.STATIC_URL))),
    url(r'^robots\.txt$', RedirectView.as_view(url='{}robots.txt'.format(settings.STATIC_URL))),


    # Django Admin
    url(r'^staff/', include(admin.site.urls)),
]




###
#
# Debugging Configuration
#
###

# Test URLs to allow you to see these pages while DEBUG is True
if getattr(settings, 'DEBUG_ERRORS', False):
    urlpatterns = patterns('mainsite.views',
        url(r'^error/404/$', 'error404', name='404'),
        url(r'^error/500/$', 'error500', name='500'),
    ) + urlpatterns

# If DEBUG_MEDIA is set, have django serve anything in MEDIA_ROOT at MEDIA_URL
if getattr(settings, 'DEBUG_MEDIA', True):
    media_url = getattr(settings, 'MEDIA_URL', '/media/').lstrip('/')
    urlpatterns = patterns('',
        url(r'^%s(?P<path>.*)$' % (media_url,), 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        }),
    ) + urlpatterns

# If DEBUG_STATIC is set, have django serve up static files even if DEBUG=False
if getattr(settings, 'DEBUG_STATIC', True):
    static_url = getattr(settings, 'STATIC_URL', '/static/').lstrip('/')
    urlpatterns = patterns('',
        url(r'^%s(?P<path>.*)' % (static_url,), 'django.contrib.staticfiles.views.serve', kwargs={
            'insecure': True,
        })
    ) + urlpatterns
