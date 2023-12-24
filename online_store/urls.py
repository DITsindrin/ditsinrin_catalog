from django.urls import path
from online_store.apps import OnlineStoreConfig

from .views import home, contacts, base_test, ProductListView, ProductDetailView, ProductCreateView, ProductDeleteView, \
    ProductUpdateView

app_name = OnlineStoreConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products-create/', ProductCreateView.as_view(), name='product-create'),
    path('product-edit/<int:pk>/', ProductUpdateView.as_view(), name='product-edit'),
    path('product-delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('base/', base_test, name='base'),
]