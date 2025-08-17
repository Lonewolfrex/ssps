from django.db import models
from orders.models import Order

class RazorpayOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='razorpay')
    rp_order_id = models.CharField(max_length=120, blank=True, default="")
    rp_payment_id = models.CharField(max_length=120, blank=True, default="")
    rp_signature = models.CharField(max_length=200, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Razorpay {self.rp_order_id} for Order {self.order_id}"
