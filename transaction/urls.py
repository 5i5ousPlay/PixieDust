from django.urls import path
from .views import TransactionListView, TransactionCreate

urlpatterns = [
    path('list/', TransactionListView.as_view(), name='transaction-list'),
    path('create/', TransactionCreate.as_view(), name='transaction-create'),
]
