from django.contrib import admin
from .models import Expense, Vendor

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date','type','category','vendor','amount','created_by')
    list_filter = ('type','date','vendor')
    search_fields = ('category','notes')

admin.site.register(Vendor)
