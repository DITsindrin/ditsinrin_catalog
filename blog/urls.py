from django.urls import path
from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig

from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='blogs'),
    path('blog-detail/<int:pk>', ArticleDetailView.as_view(), name='blog-detail'),
    path('blog-create/', never_cache(ArticleCreateView.as_view()), name='blog-create'),
    path('blog-edit/<int:pk>', never_cache(ArticleUpdateView.as_view()), name='blog-edit'),
    path('blog-delete/<int:pk>', never_cache(ArticleDeleteView.as_view()), name='blog-delete'),
]
