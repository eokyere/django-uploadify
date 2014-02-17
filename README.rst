README
======

USAGE:
------

.. code-block:: html

    {% load uploadify_tags %}
    <html>
    <head>{% uploadify_css %}</head>
    <body>
    {% uploadify_element "uploadify_id" "file" %}
    {% uploadify_scripts "uploadify_id" "/upload/" %}
    </body>
    </html>
