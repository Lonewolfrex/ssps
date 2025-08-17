from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name

class Expense(models.Model):
    TYPE_CHOICES = [
        ('CAPEX','Capital Expenditure'),
        ('OPEX','Operating Expenditure'),
    ]
    date = models.DateField()
    type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    category = models.CharField(max_length=120)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    attachment = models.FileField(upload_to='expenses/', blank=True, null=True)

    def __str__(self):
        return f"{self.date} {self.type} {self.category} ₹{self.amount}"
