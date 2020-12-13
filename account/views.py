from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from account.forms import EditProfileAccountForm, LoginAccountForm, RegisterAccountForm
from account.models import Profile
from news.models import News


class ProfileAccount(DetailView):
    model = User
    template_name = 'account/detail_profile.html'
    context_object_name = 'user_profile'
    queryset = User.objects.select_related('profile')


class EditProfileAccount(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = EditProfileAccountForm
    context_object_name = 'user_profile'
    login_url = reverse_lazy('account:login')
    template_name = 'account/edit_profile.html'

    def get_queryset(self):
        return Profile.objects.filter(user=self.kwargs['user_id']).select_related('user')

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.kwargs['user_id'])

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class RegisterAccount(CreateView):
    model = News
    form_class = RegisterAccountForm
    template_name = 'account/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            Profile.objects.create(user=User.objects.get(username=form.cleaned_data['username']))
            messages.success(self.request, 'Вы успешно зарегистрировались')
            return redirect(reverse_lazy('account:login') + '?next=/news/')
        else:
            messages.error(self.request, 'Ошибка регистрации')
            return render(request, self.template_name, {'form': form})


class LoginAccount(SuccessMessageMixin, LoginView):
    form_class = LoginAccountForm
    template_name = 'account/login.html'
    success_message = f'Вы успешно авторизировались'


class LogoutAccount(SuccessMessageMixin, LogoutView):
    success_message = 'Вы успешно вышли из аккаунта'
    template_name = 'account/logout.html'
