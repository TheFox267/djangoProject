# -*- coding: utf-8 -*-
from django.urls import path

from news.views import AddNews, AllNews, DeleteNews, DetailCategory, DetailNews, DetailUserNews, EditNews, Feedback

app_name = 'news'
urlpatterns = [
    path('', AllNews.as_view(), name='all_news'),
    path('<int:pk>/', DetailNews.as_view(), name='detail_news'),
    path('<int:category_id>', DetailCategory.as_view(), name='detail_category'),
    path('user/<int:user_id>/news', DetailUserNews.as_view(), name='detail_user_news'),
    path('add_news/', AddNews.as_view(), name='add_news'),
    path('edit/<int:pk>/', EditNews.as_view(), name='edit_news'),
    path('delete/<int:pk>/', DeleteNews.as_view(), name='delete_news'),
    path('feedback/', Feedback.as_view(), name='feedback'),
]
