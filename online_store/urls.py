from django.urls import path
from online_store.apps import OnlineStoreConfig

from .views import home, contacts, products, product_detail, product_create, base_test

app_name = OnlineStoreConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),
    path('product-detail/<int:pk>', product_detail, name='product-detail'),
    path('products-create/', product_create, name='product-create'),
    path('base/', base_test, name='base'),
]