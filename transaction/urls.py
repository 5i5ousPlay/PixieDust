from django.urls import path
from .views import TransactionListView

urlpatterns = [
    path('list/', TransactionListView.as_view(), name='transaction-list'),
]
