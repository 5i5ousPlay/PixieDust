from django.urls import path
from .views import OrderItemCreate, OrderCreate

urlpatterns = [
    path('itemcreate/', OrderItemCreate.as_view(), name='orderitem-create'),
    path('create/', OrderCreate.as_view(), name='order-create'),
]
