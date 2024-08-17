from . import jalali
from django.utils import timezone
from django.utils.html import format_html
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def custom_pagination(context):
    is_paginated = context.get('is_paginated', False)
    page_obj = context.get('page_obj', None)
    category = context.get('category', None)

    if not is_paginated or not page_obj or not category:
        return ''

    html = ''
    if page_obj.has_previous():
        html += f'<a class="btn btn-primary float-right ml-3" href="{context["request"].build_absolute_uri(f"/blog/category/{category.slug}/{page_obj.previous_page_number}/")}">پست های بعدی</a>'

    if page_obj.has_next():
        html += f'<a class="btn btn-primary float-right ml-3" href="{context["request"].build_absolute_uri(f"/blog/category/{category.slug}/{page_obj.next_page_number}/")}">پست های قبلی</a>'

    return html


def persian_number_converter(mystr):
    numbers = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }

    for e, p in numbers.items():
        mystr = mystr.replace(e, p)
    return mystr


def jalali_converter(time):
    jmonths = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']

    time = timezone.localtime(time)

    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()

    time_to_list = list(time_to_tuple)

    for index, month in enumerate(jmonths):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break
    output = f"{time_to_list[2]} {time_to_list[1]} {time_to_list[0]}ساعت {time.hour}:{time.minute}"

    return persian_number_converter(output)

