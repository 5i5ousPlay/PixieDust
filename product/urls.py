from django.urls import path
from .views import RegisterProduct, ProductListView

urlpatterns = [
    path('register/', RegisterProduct.as_view(), name='product-register'),
    path('list/', ProductListView.as_view(), name='product-list'),
]