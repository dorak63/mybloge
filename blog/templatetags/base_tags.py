from django import template
from ..models import Category


register = template.Library()


# @register.simple_tag(takes_context=True)
# def custom_pagination(context):
#     is_paginated = context.get('is_paginated', False)
#     page_obj = context.get('page_obj', None)
#     category = context.get('category', None)
#
#     if not is_paginated or not page_obj or not category:
#         return ''
#
#     html = ''
#     if page_obj.has_previous():
#         html += f'<a class="btn btn-primary float-right ml-3" href="{context["request"].build_absolute_uri(f"/blog/category/{category.slug}/{page_obj.previous_page_number}/")}">پست های بعدی</a>'
#
#     if page_obj.has_next():
#         html += f'<a class="btn btn-primary float-right ml-3" href="{context["request"].build_absolute_uri(f"/blog/category/{category.slug}/{page_obj.next_page_number}/")}">پست های قبلی</a>'
#
#     return html


@register.simple_tag
def title():
    return "وبلاگ کسب درآمدی"


@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    return {
        "category": Category.objects.filter(status=True)
    }
