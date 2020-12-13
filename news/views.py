# Create your views here.
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from news.forms import AddNewsForm, FeedbackForm
from news.models import Category, News


class AllNews(ListView):
    """
    Выводит список всех новостей на главной странице
    Модель: News
    Шаблон: 'news/all_news.html'
    Ключ в контексте: 'all_news'
    Количество новостей на одной странице: 4
    Запрос: Объект News с фильтрацией по статусу публикации, при этом используется "жадное присоединение" полей "category","author"
    и сортировка, чтобы самые свежие новости были сверху
    """
    model = News
    template_name = 'news/all_news.html'
    context_object_name = 'all_news'
    paginate_by = 4
    queryset = News.objects.filter(is_published=True).select_related('category', 'author').order_by('-created_at')
    allow_empty = False


class DetailCategory(ListView):
    """
    Выводит список новостей по определённой категории
    """
    model = News
    template_name = 'news/detail_category.html'
    context_object_name = 'detail_category'
    paginate_by = 4
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DetailCategory, self).get_context_data(**kwargs)
        context['title_category'] = Category.objects.get(pk=self.kwargs['category_id']).title
        return context

    def get_queryset(self):
        return News.objects.filter(category=self.kwargs['category_id'], is_published=True).select_related('author').order_by('-created_at')


class DetailUserNews(ListView):
    """
    Выводит список всех новостей у определённого пользователя
    """
    model = News
    template_name = 'news/detail_user_news.html'
    context_object_name = 'detail_user_news'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(author=self.kwargs['user_id'], is_published=True).select_related('category').order_by('-created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DetailUserNews, self).get_context_data(**kwargs)
        # context['author_name'] = News.objects.filter(author=self.kwargs['user_id'])[0].author.username
        context['author_name'] = User.objects.filter(pk=self.kwargs['user_id'])[0]
        return context


class DetailNews(DetailView):
    """
    Выводит одну новость со всей информацией о ней
    """
    model = News
    template_name = 'news/detail_news.html'
    context_object_name = 'detail_news'

    def get_queryset(self):
        model = News.objects.select_related('category', 'author').get(pk=self.kwargs['pk'])
        if self.request.user.id == model.author.id:
            return News.objects.filter(pk=self.kwargs['pk']).select_related('category', 'author')
        else:
            return News.objects.filter(pk=self.kwargs['pk'], is_published=True).select_related('category', 'author')


class AddNews(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Выводит форму для создания новости
    """
    model = News
    form_class = AddNewsForm
    template_name = 'news/add_news.html'
    login_url = reverse_lazy('account:login')
    success_message = "Новость успешна создана"
    queryset = News.objects.select_related('category')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddNews, self).form_valid(form)


class EditNews(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    Выводит форму для редактирования существующих новостей
    """
    model = News
    form_class = AddNewsForm
    template_name = 'news/edit_news.html'
    context_object_name = 'news'
    success_message = 'Ваша новость успешно отредактирована'
    login_url = reverse_lazy('account:login')

    def test_func(self):
        obj = self.get_object()
        return obj.author.id == self.request.user.id


class DeleteNews(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = News
    success_message = 'Ваша новость успешно удалена'
    template_name = 'news/delete_news.html'
    login_url = reverse_lazy('account:login')
    context_object_name = 'delete_news'
    success_url = reverse_lazy('news:all_news')

    def test_func(self):
        obj = self.get_object()
        return obj.author.id == self.request.user.id


class Feedback(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Выводит форму для отправки обращения на почту
    """
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
                messages.success(request, 'Ваше обращение успешно отправлено')
                messages.success(request, 'Спасибо за ваш отзыв')
                return redirect('news:feedback')
            else:
                messages.error(request, 'Ошибка при отправке письма')
                return render(request, template_name=self.template_name, context={'form': form})
