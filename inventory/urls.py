from django.urls import path
from .views import InventoryCreateView, InventoryListView

urlpatterns = [
    path('create/', InventoryCreateView.as_view(), name='inventory-create'),
    path('list/', InventoryListView.as_view(), name='inventory-list'),
]
