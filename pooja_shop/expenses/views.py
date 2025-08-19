from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum
from .models import Expense, Vendor

def staff_required(view):
    return user_passes_test(lambda u: u.is_staff)(view)

@login_required
@staff_required
def expenses_dashboard(request):
    total_capex = Expense.objects.filter(type='CAPEX').aggregate(Sum('amount'))['amount__sum'] or 0
    total_opex = Expense.objects.filter(type='OPEX').aggregate(Sum('amount'))['amount__sum'] or 0
    recent = Expense.objects.order_by('-date')[:10]
    return render(request, 'expenses/dashboard.html', {
        'total_capex': total_capex,
        'total_opex': total_opex,
        'recent': recent,
    })

@login_required
@staff_required
def expense_add(request):
    if request.method == 'POST':
        exp = Expense.objects.create(
            date = request.POST.get('date') or timezone.now().date(),
            type = request.POST.get('type'),
            category = request.POST.get('category'),
            amount = request.POST.get('amount') or 0,
            notes = request.POST.get('notes',''),
            created_by = request.user
        )
        messages.success(request, 'Expense logged')
        return redirect('expenses_dashboard')
    return render(request, 'expenses/expense_add.html')

