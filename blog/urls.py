from django.urls import path
from blog.apps import BlogConfig

from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='blogs'),
    path('blog-detail/<int:pk>', ArticleDetailView.as_view(), name='blog-detail'),
    path('blog-create/', ArticleCreateView.as_view(), name='blog-create'),
    path('blog-edit/<int:pk>', ArticleUpdateView.as_view(), name='blog-edit'),
    path('blog-delete/<int:pk>', ArticleDeleteView.as_view(), name='blog-delete'),
]
