from django.urls import path

from news.views import AddNews, AllNews, DetailCategory, DetailNews, EditNews, Feedback

app_name = 'news'
urlpatterns = [
    path('', AllNews.as_view(), name='all_news'),
    path('<int:pk>/', DetailNews.as_view(), name='detail_news'),
    path('category/<int:category_id>', DetailCategory.as_view(), name='detail_category'),
    path('add_news/', AddNews.as_view(), name='add_news'),
    path('feedback/', Feedback.as_view(), name='feedback'),
    path('edit_news/<int:pk>', EditNews.as_view(), name='edit_news'),
]
