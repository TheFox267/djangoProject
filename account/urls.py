from django.urls import path

from account.views import RegisterAccount, LoginAccount

app_name = 'account'
urlpatterns = [
    path('register/', RegisterAccount.as_view(), name='register'),
    path('login/', LoginAccount.as_view(), name='login'),
]
