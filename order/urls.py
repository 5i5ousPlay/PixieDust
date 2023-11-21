from django.urls import path
from .views import OrderItemCreate, OrderCreate, OrderList

urlpatterns = [
    path('itemcreate/', OrderItemCreate.as_view(), name='orderitem-create'),
    path('create/', OrderCreate.as_view(), name='order-create'),
    path('list/', OrderList.as_view(), name='order-list'),
]
