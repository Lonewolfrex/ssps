from django.urls import path
from . import views

urlpatterns = [
    path('create-razorpay-order/<int:order_id>/', views.create_razorpay_order, name='create_razorpay_order'),
    path('webhook/', views.razorpay_webhook, name='razorpay_webhook'),
]
