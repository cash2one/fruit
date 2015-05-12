# coding=utf-8
from django import template
import datetime, time

import re
from django.shortcuts import get_object_or_404

register = template.Library()

"""
Requirement:
{%load util_tags%}

System build in https://docs.djangoproject.com/en/dev/ref/templates/builtins/
"""

#针对state
@register.filter
def dict_get(dict, key):
    """How to Use

    {{ dict|dict_get:key }}

    """

    return dict.get(key, '')


@register.filter
def index_url(value,str):

    if str in value:
        return True
    else:
        return False

@register.filter
def lower(value):  # Only one argument.
    """Converts a string into all lowercase
        How to Use
        {{ value|lower|lower|.... }}
    """
    return value.lower()


@register.filter
def upper(value):  # Only one argument.
    """Converts a string into all lowercase
        How to Use
        {{ value|lower|lower|.... }}
    """
    return value.upper()



@register.filter
def to_int(value):  # Only one argument.
    if value and len(value) > 0:
        result = int(value)
    else:
        result = 0
    return result


@register.filter
def type_of(value):  # Only one argument.
    return type(value)


@register.assignment_tag
def get_current_time(format_string):
    """
    How to Use
    You may then store the result in a template variable using the as argument followed by the variable name, and output it yourself where you see fit:
    {% get_current_time "%Y-%m-%d %I:%M %p" as the_time %}
    <p>The time is {{ the_time }}.</p>
    """
    return datetime.datetime.now().strftime(format_string)


