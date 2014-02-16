README
======

USAGE:
------

.. code-block:: html

    {% load uploadify_tags %}
    <html>
        <head>{% uploadify_css %}</head>
        <body>
            <form action="{{request.path}}" method="POST">
                {% csrf_token %}
                {% uploadify_element "uploadify" "file" %}
            </form>
            {% uploadify_scripts "uploadify" request.path %}
        </body>
    </html>
