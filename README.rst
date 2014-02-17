README
======

A basic uploadify wrapper for django framework.

USAGE:
******

urls.py:

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^', include('uploadify.urls')),
        ...
    )

settings.py:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'uploadify',
        ...
    )   

    UPLOADIFY_UPLOAD_PATH = "uploads"

In your application's templates:

.. code-block:: html

    {% load uploadify_tags %}
    <html>
    <head>{% uploadify_css %}</head>
    <body>
    {% uploadify_element "uploadify_id" "file" %}
    {% uploadify_scripts "uploadify_id" "/upload/" %}
    </body>
    </html>
