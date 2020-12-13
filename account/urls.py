from django.urls import path

from account.views import LoginAccount, LogoutAccount, ProfileAccount, RegisterAccount

app_name = 'account'
urlpatterns = [
    path('register/', RegisterAccount.as_view(), name='register'),
    path('login/', LoginAccount.as_view(), name='login'),
    path('logout/', LogoutAccount.as_view(), name='logout'),
    path('user/<int:pk>/', ProfileAccount.as_view(), name='profile_user'),
]
