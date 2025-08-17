from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.conf import settings
import razorpay, hmac, hashlib
from orders.models import Order
from .models import RazorpayOrder

def create_razorpay_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, status='created')
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    data = {"amount": int(order.total_amount * 100), "currency": "INR", "receipt": f"order_{order.id}"}
    rp_order = client.order.create(data=data)
    rpo, _ = RazorpayOrder.objects.get_or_create(order=order)
    rpo.rp_order_id = rp_order.get("id","")
    rpo.save()
    return JsonResponse({"order_id": rpo.rp_order_id, "key_id": settings.RAZORPAY_KEY_ID})

@csrf_exempt
def razorpay_webhook(request):
    # Minimal placeholder
    return HttpResponse("ok")
