from django import template
import datetime
register = template.Library()

@register.filter()
def hasFB(post):
    if post.date>datetime.date(2020,5,31):
        return True
    else:
        return False
