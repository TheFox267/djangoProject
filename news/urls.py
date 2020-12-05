from django.urls import path

from news.views import AllNews

app_name = 'news'
urlpatterns = [
    path('', AllNews.as_view(), name='all_news')
]
