from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Category

def home(request):
    products = Product.objects.filter(is_active=True)[:8]
    return render(request, "home.html", {"products": products})

def product_list(request, slug=None):
    category = None
    products = Product.objects.filter(is_active=True)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request, "shop/product_list.html", {"products": products, "category": category})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "shop/product_detail.html", {"product": product})

def cart_detail(request):
    cart = request.session.get("cart", {})
    items = []
    total = 0
    for pid_str, qty in cart.items():
        p = get_object_or_404(Product, id=int(pid_str))
        subtotal = p.price * qty
        total += subtotal
        items.append({"product": p, "qty": qty, "subtotal": subtotal})
    return render(request, "shop/cart.html", {"items": items, "total": total})

def cart_add(request, product_id):
    cart = request.session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session["cart"] = cart
    messages.success(request, "Added to cart.")
    return redirect("cart_detail")

def cart_remove(request, product_id):
    cart = request.session.get("cart", {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session["cart"] = cart
        messages.info(request, "Removed from cart.")
    return redirect("cart_detail")

def checkout(request):
    # Placeholder: create order in orders app
    return render(request, "shop/checkout.html")
