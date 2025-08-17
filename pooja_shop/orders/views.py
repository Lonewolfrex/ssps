from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from decimal import Decimal
from shop.models import Product
from .models import Order, OrderItem, Address

@login_required
@transaction.atomic
def create_order(request):
    # Simple order creation from session cart
    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect("product_list")
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        line1 = request.POST.get("line1")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")

        addr = Address.objects.create(user=request.user, name=name, phone=phone, line1=line1, line2="", city=city, state=state, pincode=pincode)
        order = Order.objects.create(user=request.user, shipping_address=addr, status='created')
        total = Decimal('0.00')
        for pid_str, qty in cart.items():
            p = get_object_or_404(Product, id=int(pid_str))
            qty = int(qty)
            OrderItem.objects.create(order=order, product=p, quantity=qty, price=p.price)
            total += p.price * qty
            # reduce stock
            if p.stock >= qty:
                p.stock -= qty
                p.save()
        order.total_amount = total
        order.save()
        # clear cart
        request.session["cart"] = {}
        return redirect("order_success", order_id=order.id)
    return render(request, "orders/checkout_form.html")

@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "orders/order_success.html", {"order": order})
