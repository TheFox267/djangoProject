from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView

from account.forms import RegisterAccountForm


class RegisterAccount(CreateView):
    form_class = RegisterAccountForm
    template_name = 'account/register.html'

    def form_valid(self, form):
        return redirect('account:login')


class LoginAccount(CreateView):
    pass
