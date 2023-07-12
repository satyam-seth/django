import datetime
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


# ### Filters ### #


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


# ### Tags ### #


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

# @register.simple_tag(takes_context=True)
# def current_time(context, format_string):
#     timezone = context["timezone"]
#     return your_get_current_time_method(timezone, format_string)


register.simple_tag(lambda x: x - 1, name="minusone")


@register.simple_tag(name="minustwo")
def some_function(value):
    return value - 2


@register.simple_tag
def my_tag(a, b, *args, **kwargs):
    warning = kwargs["warning"]
    profile = kwargs["profile"]


@register.inclusion_tag("results.html")
def show_results(poll):
    choices = poll.choice_set.all()
    return {"choices": choices}
