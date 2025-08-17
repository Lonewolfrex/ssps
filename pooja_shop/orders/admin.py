from django.contrib import admin
from .models import Address, Order, OrderItem, Coupon

admin.site.register(Address)
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id","user","status","total_amount","created_at")
    list_filter = ("status","created_at")
    inlines = [OrderItemInline]

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ("code","discount_percent","active")
    list_editable = ("discount_percent","active")
