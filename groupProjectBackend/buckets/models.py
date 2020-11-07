from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Bucket(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50, blank=True)
    icon = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=1)
    # min_amt = models.FloatField(blank=True, null=True)
    percentage = models.IntegerField()
    parent_bucket = models.ForeignKey(
        'self', 
        related_name = 'children',
        on_delete=models.CASCADE, 
        blank=True, null=True
        )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='buckets'
    )

        
    def __str__(self):
        return self.name

    def display_children(self):
        """This is required for Admin display."""
        return ', '.join(children.name for children in self.children.all()[:3])    
    display_children.short_description = 'Children'


    def display_expense(self):
        """This is required for Admin display."""
        return ', '.join(expense.name for expense in self.expenses.all()[:3])    
    display_expense.short_description = 'Expenses'
    
    class Meta:
        ordering = ['id']

    @property
    def min_amt(self):
        expenses = Expense.objects.filter(bucket = self.id)
        expenses_total = 0
        for expenses in expenses:
            expenses_total = expenses_total + expenses.monthly_exp_amt
        return expenses_total


class Transaction(models.Model):
    income = models.FloatField()
    date_created =  models.DateTimeField(auto_now_add=True)
    receipt = models.CharField(max_length=5000)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='transactions'
    )

    class Meta:
        ordering = ['-id']


class Expense(models.Model):
    name = models.CharField(max_length=50)
    monthly_exp_amt = models.FloatField()
    bucket = models.ForeignKey(
        Bucket,
        related_name = 'expenses',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='expenses',
        
    )

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name