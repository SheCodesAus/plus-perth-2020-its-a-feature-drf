from django.contrib import admin
from .models import Bucket, Transaction, Expense

@admin.register(Bucket)
class BucketAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent_bucket', 'display_children', 'display_expense', 'is_active']
    list_filter = ("owner","is_active")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'income', 'receipt', 'date_created']
    list_filter = ("owner", "owner__is_active")


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    # list_filter = ("bucket", "bucket__is_active", "owner")