# Create your views here.
from django.views.generic import ListView

from news.models import News


class AllNews(ListView):
    model = News
    template_name = 'news/all_news.html'
    context_object_name = 'all_news'
