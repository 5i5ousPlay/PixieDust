from django.urls import path
from .views import RegisterProduct, ProductListView, ProductDetailView, ProductDeleteView

urlpatterns = [
    path('register/', RegisterProduct.as_view(), name='product-register'),
    path('list/', ProductListView.as_view(), name='product-list'),
    path('detail/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('delete/<int:id>/', ProductDeleteView.as_view(), name='product-delete'),
]
