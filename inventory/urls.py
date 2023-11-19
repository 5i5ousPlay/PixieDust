from django.urls import path
from .views import InventoryCreateView, InventoryListView, InventoryDetailView, InventoryDeleteView

urlpatterns = [
    path('create/', InventoryCreateView.as_view(), name='inventory-create'),
    path('list/', InventoryListView.as_view(), name='inventory-list'),
    path('detail/<int:id>/', InventoryDetailView.as_view(), name='inventory-detail'),
    path('delete/<int:id>/', InventoryDeleteView.as_view(), name='inventory-delete'),
]
