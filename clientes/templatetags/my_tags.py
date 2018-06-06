from django import template
from datetime import datetime
register = template.Library()


@register.simple_tag
def minhatag(format_string):
    return datetime.now().strftime(format_string)

