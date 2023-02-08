from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('article_list/', ArticleListView.as_view(), name='article_list'),
    path('article_detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article_create/', ArticleCreateView.as_view(), name='article_create'),
    path('article_update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('article_delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete')
]