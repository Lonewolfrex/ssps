from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.expenses_dashboard, name='expenses_dashboard'),
    path('add/', views.expense_add, name='expense_add'),
]
