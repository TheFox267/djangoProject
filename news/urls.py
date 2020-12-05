from django.urls import path

from news.views import AllNews, DetailNews, DetailCategory

app_name = 'news'
urlpatterns = [
    path('', AllNews.as_view(), name='all_news'),
    path('<int:pk>/', DetailNews.as_view(), name='detail_news'),
    path('category/<int:category_id>', DetailCategory.as_view(), name='detail_category'),
]
