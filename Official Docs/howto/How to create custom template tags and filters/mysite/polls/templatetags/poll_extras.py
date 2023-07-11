from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from django import template

register = template.Library()


@register.filter(name="cut")
def cut(value, arg):
    """Removes all values of arg from the given string"""
    print(value)
    return value.replace(arg, "")


@register.filter
@stringfilter
def lower(value):  # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


@register.filter(is_safe=True)
def add_xx(value):
    return "%sxx" % value


@register.filter(needs_autoescape=True)
def initial_letter_filter(text, autoescape=True):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        def esc(x): return x
    result = "<strong>%s</strong>%s" % (esc(first), esc(other))
    return mark_safe(result)


@register.filter(expects_localtime=True)
def businesshours(value):
    try:
        return 9 <= value.hour < 17
    except AttributeError:
        return ""
