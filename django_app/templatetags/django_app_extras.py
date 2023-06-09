from django import template
import datetime


register = template.Library()


@register.simple_tag(takes_context=True)
def text_upper_case(context, text: str):
    try:
        return str(text).upper()
    except Exception as error:
        print("error simple_tag text_upper_case: ", error)
        return ""


@register.simple_tag(takes_context=True)
def access_tag(context, slug: str):
    user = context["request"].user
    return user.is_authenticated


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.filter(name="cut_string")
def cut_string(value, arg: int):
    return f"{value[0:arg]}..."


@register.filter(name="cut")
def cut(value, arg):
    return value.replace(arg, "")


@register.filter(name="lower")
def lower(value):
    return value.lower()
