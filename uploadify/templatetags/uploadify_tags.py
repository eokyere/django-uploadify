from django import template
from uploadify import settings

register = template.Library()

@register.inclusion_tag('uploadify/css.html', takes_context=True)
def uploadify_css(context):
    return { 'uploadify_path' : settings.UPLOADIFY_PATH,}

@register.inclusion_tag('uploadify/scripts.html', takes_context=True)
def uploadify_scripts(context, uploadify_id, serverside_path):
    return { 'uploadify_id' : uploadify_id, 'uploadify_path' : settings.UPLOADIFY_PATH, 'uploadify_serverside_path' : serverside_path, }

@register.inclusion_tag('uploadify/element.html', takes_context=True)
def uploadify_element(context, uploadify_id, form_name):
    return { 'uploadify_id' : uploadify_id, 'uploadify_form_name': form_name, }
