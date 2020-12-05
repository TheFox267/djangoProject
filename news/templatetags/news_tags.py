from django import template
from django.db.models import Count

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_list_category')
def get_categories():
    categories = Category.objects.annotate(cnt=Count('news'))
    return categories
