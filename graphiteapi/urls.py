#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Urls for the API.  These will be anchored at /api/ if you have followed the
installation instructions in the README."""

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('graphiteapi.views',
    ('^stats/list/?', 'stats_list'),
    ('', 'index'),
)
