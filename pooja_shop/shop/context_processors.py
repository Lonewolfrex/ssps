from .models import Category

def categories(request):
    return {"all_categories": Category.objects.all()}

def cart_item_count(request):
    cart = request.session.get("cart", {})
    return {"cart_item_count": sum(cart.values())}


def brand(request):
    return {
        "BRAND_NAME": "Satvik Sparsh Pooja Store",
        "BRAND_TAGLINE": "Divine Essentials, Delivered",
        "BRAND_COLOR": "#ffc766",  # light saffron
    }
