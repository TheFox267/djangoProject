from django.urls import path

from news.views import AllNews, DetailNews

app_name = 'news'
urlpatterns = [
    path('', AllNews.as_view(), name='all_news'),
    path('<int:pk>/', DetailNews.as_view(),name='detail_news')
]
