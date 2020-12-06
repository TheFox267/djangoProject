# Create your views here.
from django.conf import settings
from django.views.generic import ListView, DetailView, CreateView

from news.forms import AddNewsForm, FeedbackForm
from news.models import News, Category
from django.core.mail import send_mail



class AllNews(ListView):
    model = News
    template_name = 'news/all_news.html'
    context_object_name = 'all_news'
    paginate_by = 4

    def get_queryset(self):
        return News.objects.filter(is_published=True).order_by('-created_at')


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
    paginate_by = 4

    def get_queryset(self):
        return News.objects.filter(category=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DetailCategory, self).get_context_data(**kwargs)
        context['title_category'] = Category.objects.get(pk=self.kwargs['category_id']).title
        return context


class AddNews(CreateView):
    form_class = AddNewsForm
    template_name = 'news/add_news.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddNews, self).form_valid(form)


class FeedbackNews(CreateView):
    form_class = FeedbackForm
    template_name = 'news/feedback.html'

    def form_valid(self, form):
        return super(FeedbackNews, self).form_valid(form)
    # def form_valid(self, form):
    #     print(self.request.user.email)
    #     mail = send_mail(form.cleaned_data['title'], form.cleaned_data['content'], settings.EMAIL_HOST_USER, [self.request.user.email], fail_silently=False)
    #     if mail:
    #         print('good')
    #     else:
    #         print('bad')
