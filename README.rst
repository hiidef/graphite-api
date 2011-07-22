graphite-api
-----------

This package implements a json API to various graphite data.  You should install
via pip::

    pip install https://github.com/hiidef/graphite-api/tarball/master

And then make the following changes to your graphite installation:

* modify ``INSTALLED_APPS`` to include ``graphiteapi``
* add graphite-api's urls to ``grahpite/urls.py``::
    ('^api/?', include('graphiteapi.urls'))

You should now be able to hit ``http://your.graphite.server/api/`` for a simple
JSON api to various data contained within your graphite server.

