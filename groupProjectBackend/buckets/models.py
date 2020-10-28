from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Bucket(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50, blank=True)
    icon = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=1)
    min_amt = models.FloatField(blank=True, null=True)
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
        return ', '.join(children.name for children in self.children.all()[:3])
    
    display_children.short_description = 'Children'
    
    class Meta:
        ordering = ['id']


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