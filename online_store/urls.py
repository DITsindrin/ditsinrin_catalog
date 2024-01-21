from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from online_store.apps import OnlineStoreConfig

from .views import home, contacts, base_test, ProductListView, ProductDetailView, ProductCreateView, ProductDeleteView, \
    ProductUpdateView

app_name = OnlineStoreConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product-detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product-detail'),
    path('products-create/', never_cache(ProductCreateView.as_view()), name='product-create'),
    path('product-edit/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='product-edit'),
    path('product-delete/<int:pk>/', never_cache(ProductDeleteView.as_view()), name='product-delete'),
    path('base/', base_test, name='base'),
]