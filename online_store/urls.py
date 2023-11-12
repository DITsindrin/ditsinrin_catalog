from django.urls import path
from online_store.apps import OnlineStoreConfig

from .views import home, contacts

app_name = OnlineStoreConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]