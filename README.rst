README
======

.. image:: https://badge.fury.io/py/django-settings.png
   :target: https://badge.fury.io/py/django-settings

.. image:: https://api.travis-ci.org/jqb/django-settings.png?branch=master
   :target: https://travis-ci.org/jqb/django-settings

settings.py:
------------

.. code-block: python

    MIDDLEWARE_CLASSES = (
    ...
    'uploadify.middleware.SWFUploadMiddleware',
    ...
    }
