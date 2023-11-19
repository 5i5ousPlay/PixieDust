from django.urls import path
from .views import InventoryCreateView

urlpatterns = [
    path('create/', InventoryCreateView.as_view(), name='inventory-create'),
]