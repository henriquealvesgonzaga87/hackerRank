from django.core.management.base import BaseCommand
from models import Product


class Command(BaseCommand):
    help = "List products with low stock"

    def add_arguments(self, parser):
        parser.add_argument("threshold", type=int)

    def handle(self, * args, ** options):
        threshold = options["threshold"]
        low_stock_products = Product.objects.filter(quantity__lt=threshold)
        for product in low_stock_products:
            self.stdout.write(self.style.SUCCESS(f"Low Stock: {product.name}"))
