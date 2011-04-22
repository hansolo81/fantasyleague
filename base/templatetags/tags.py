from django import template

register = template.Library()


@register.simple_tag
def current_page_item(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'current_page_item'
    return ''
