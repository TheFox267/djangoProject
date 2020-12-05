from django import template
from django.db.models import Count, F

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_list_category')
def get_categories():
    categories = Category.objects.annotate(cnt=Count('news',filter=F('news__is_published')))
    return categories
