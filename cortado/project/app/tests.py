from django.test import TestCase
from models import Customer


class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name='John', email='john@example.com')

    def test_customer_creation(self):
        customer = Customer.objects.get(name='John')
        self.assertEqual(customer.email, 'john@example.com')
