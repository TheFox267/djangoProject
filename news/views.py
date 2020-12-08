# Create your views here.

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from news.forms import AddNewsForm, FeedbackForm
from news.models import Category, News


class AllNews(ListView):
    model = News
    template_name = 'news/all_news.html'
    context_object_name = 'all_news'
    paginate_by = 4
    queryset = News.objects.filter(is_published=True).select_related('category', 'author').order_by('-created_at')


class DetailNews(DetailView):
    model = News
    template_name = 'news/detail_news.html'
    context_object_name = 'detail_news'
    queryset = News.objects.select_related('author', 'category')


class DetailCategory(ListView):
    model = News
    template_name = 'news/detail_category.html'
    context_object_name = 'detail_category'
    paginate_by = 4
    queryset = News.objects.select_related('author').order_by('-created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DetailCategory, self).get_context_data(**kwargs)
        context['title_category'] = Category.objects.get(pk=self.kwargs['category_id']).title
        return context


class AddNews(LoginRequiredMixin, CreateView):
    form_class = AddNewsForm
    template_name = 'news/add_news.html'
    login_url = reverse_lazy('account:login')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddNews, self).form_valid(form)


class Feedback(LoginRequiredMixin, CreateView):
    form_class = FeedbackForm
    template_name = 'news/feedback.html'
    login_url = reverse_lazy('account:login')

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            mail = send_mail(subject=f"{form.cleaned_data['subject']}(id = {request.user.id}, username = {request.user.username})", message=form.cleaned_data['content'],
                             from_email=request.user.email, recipient_list=settings.EMAIL_HOST_USER.split(' '), fail_silently=False)
            if mail:
                messages.success(request, 'Письмо успешно отправлено')
                messages.success(request, 'Спасибо за ваш отзыв')
                return redirect('news:feedback')
            else:
                messages.error(request, 'Ошибка при отправке письма')
                return render(request, template_name=self.template_name, context={'form': form})


class EditNews(UpdateView):
    model = News
    form_class = AddNewsForm
    template_name = 'news/edit_news.html'
