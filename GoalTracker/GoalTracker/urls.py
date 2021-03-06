"""
Definition of urls for GoalTracker.
"""

from datetime import datetime
from django.conf.urls import include, url
from django.contrib import admin
import django.contrib.auth.views

import goalie.forms
import goalie.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', goalie.views.home, name='home'),
    url(r'^contact$', goalie.views.contact, name='contact'),
    url(r'^about', goalie.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'goalie/login.html',
            'authentication_form': goalie.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^goalie/', include('goalie.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
