from django.urls import path
from .views import ArticleListView

urlpatterns = [
    path('article_list/', ArticleListView.as_view(), name='article_list')
]