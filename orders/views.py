from django.shortcuts import render


from .models import Order


# Create your views here.


class RegisterOrder(generics.CreateAPIView):
    queryset = Order.objects.all()


class OrderSubclassMixin(object):
    def get_queryset(self):
        return Order.objects.select_subclasses()


class OrderDetailView(OrderSubclassMixin, generics.RetrieveUpdateAPIView):

    lookup_field = 'id'


class OrderDeleteView(OrderSubclassMixin, generics.DestroyAPIView):

    lookup_field = 'id'
