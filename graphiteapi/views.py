#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Graphite-api views."""

try:
    import simplejson as json
except:
    import json

import os
from functools import wraps
from django.http import HttpResponse
from os.path import splitext
from django.conf import settings

class JsonResponse(HttpResponse):
    """Simple django HttpResponse object that can take some json data."""
    def __init__(self, *args, **kwargs):
        args = list(args)
        if not isinstance(args[0], basestring):
            args[0] = json.dumps(args[0])
        # FIXME: use text/json when not in development
        kwargs['mimetype'] = 'text/javascript'
        super(JsonResponse, self).__init__(*args, **kwargs)

def jsonresponse(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        if isinstance(ret, HttpResponse):
            return ret
        return JsonResponse(ret)
    return wrapper

@jsonresponse
def index(request):
    return {'status': 'ok'}

@jsonresponse
def stats_list(request):
    """Returns dictionary of stat dirs to their contained whisper files, such
    that every key is a directory with a whisper file, and the values are lists
    of such whisper files.  The dirs returned use . separators, and the whisper
    db files are stripped of their extension."""
    stats = {}
    for path in settings.DATA_DIRS:
        for root, dirs, files in os.walk(path):
            statroot = root.replace(path, '')
            whisper_dbs = filter(lambda x: x.endswith('.wsp'), files)
            if whisper_dbs:
                stats[statroot.replace('/', '.')] = [splitext(w)[0] for w in whisper_dbs]
    return stats


