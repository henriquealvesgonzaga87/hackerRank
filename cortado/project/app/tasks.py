from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime
from .models import Order


@shared_task
def send_order_confirmation_email(order_id):
    order = Order.objects.get(id=order_id)
    subject = "Order Confirmation"
    message = f"Your order with id: {order_id} has been confirmed"
    recipient_list = [order.customer.email]
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Sending daily report at {current_time}")
    send_mail(subject, message, 'noreply@example.com', recipient_list)
