# Create your views here.
from django.views.generic import ListView, DetailView

from news.models import News, Category


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

    def get_queryset(self):
        return News.objects.filter(pk=self.kwargs['pk'], is_published=True)


class DetailCategory(ListView):
    model = News
    template_name = 'news/detail_category.html'
    context_object_name = 'detail_category'

    def get_queryset(self):
        return News.objects.filter(category=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DetailCategory, self).get_context_data(**kwargs)
        context['title_category'] = Category.objects.get(pk=self.kwargs['category_id']).title
        return context
