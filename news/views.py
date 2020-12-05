# Create your views here.
from django.views.generic import ListView, DetailView

from news.models import News


class AllNews(ListView):
    model = News
    template_name = 'news/all_news.html'
    context_object_name = 'all_news'

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class DetailNews(DetailView):
    model = News
    template_name = 'news/detail_news.html'
    context_object_name = 'detail_news'