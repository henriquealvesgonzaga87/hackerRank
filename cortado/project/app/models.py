from django.db import models
import json


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    class Meta:
        table_name = "product"


class Order:
    def __int__(self, order_id, customer_name, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total_amount = total_amount


# Data Serialization and Deserialization


def serialize_order(order):
    return json.dumps({
        'order_id': order.order_id,
        'customer_name': order.customer_name,
        'total_amount': order.total_amount,
    })


def deserialize_order(json_data):
    data = json.loads(json_data)
    return Order(data['order_id'], data['customer_name'], data['total_amount'])


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
