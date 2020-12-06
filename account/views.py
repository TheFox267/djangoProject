from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from account.forms import RegisterAccountForm, LoginAccountForm
from django.contrib.auth import login, logout


class RegisterAccount(CreateView):
    form_class = RegisterAccountForm
    template_name = 'account/register.html'

    def form_valid(self, form):
        return redirect('account:login')


class LoginAccount(LoginView):
    form_class = LoginAccountForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('news:all_news')

    def get_success_url(self):
        return self.success_url
