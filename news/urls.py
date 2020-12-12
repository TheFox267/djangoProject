from django.urls import path

from news.views import AddNews, AllNews, DetailCategory, DetailNews, DetailUserNews, EditNews, Feedback

app_name = 'news'
urlpatterns = [
    path('', AllNews.as_view(), name='all_news'),
    path('<int:pk>/', DetailNews.as_view(), name='detail_news'),
    path('category/<int:category_id>/news', DetailCategory.as_view(), name='detail_category'),
    path('add_news/', AddNews.as_view(), name='add_news'),
    path('feedback/', Feedback.as_view(), name='feedback'),
    path('edit/<int:pk>/', EditNews.as_view(), name='edit_news'),
    path('user/<int:user_id>/news', DetailUserNews.as_view(), name='detail_user_news'),
]
