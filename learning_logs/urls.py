"""Defines URL patterns for learning_logs."""

from django.conf.urls import url
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Redirects of all locations
    url(r'^barn/$', views.tavern, name='barn'),
    url(r'^church/$', views.tavern, name='church'),
    url(r'^market/$', views.tavern, name='market'),
    url(r'^park/$', views.tavern, name='park'),
    url(r'^residential/$', views.tavern, name='residential'),
    url(r'^tavern/$', views.tavern, name='tavern'),

    # Leads to listings of citizens personal details
    url(r'^citizen_details/$', views.citizen_details, name='citizen-details'),

    # Page with a master list of all citizens
    url(r'^citizen_roster/$', views.citizen_roster, name='citizen-roster'),

    # Confirm on termination
    url(r'^confirm/$', views.confirm, name='confirm'),

    # Overview maps page
    url(r'^map/$', views.map, name='map'),

    # Page with reports on citizens
    url(r'^reports/$', views.reports, name='reports'),
]
