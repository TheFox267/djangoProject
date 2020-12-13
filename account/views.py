from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
# Create your views here.
from django.views.generic import CreateView, DetailView

from account.forms import LoginAccountForm, RegisterAccountForm


class ProfileAccount(DetailView):
    model = User
    template_name = 'account/detail_profile.html'
    context_object_name = 'user_profile'

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['pk']).select_related('profile')


class RegisterAccount(CreateView):
    form_class = RegisterAccountForm
    template_name = 'account/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Вы успешно зарегистрировались')
            return redirect('account:login')
        else:
            messages.error(self.request, 'Ошибка регистрации')
            return render(request, self.template_name, {'form': form})


class LoginAccount(SuccessMessageMixin, LoginView):
    form_class = LoginAccountForm
    template_name = 'account/login.html'
    success_message = f'Вы успешно авторизировались'


class LogoutAccount(LogoutView):
    template_name = 'account/logout.html'
