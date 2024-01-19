from rest_framework import viewsets
from .models import Product, Order
from .serializers import ProductSerializer
from django.db.models import F, Sum


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def get_orders_for_customer(customer_id):
    orders = Order.objects.filter(customer_id=customer_id).select_related("product")
    total_quantity = orders.aggregate(total_quantity=Sum('product__quantity'))['total_quantity']
    return orders, total_quantity
