from django.db import models

# Create your models here.
class Bucket(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    is_active = models.BooleanField(default=1)
    min_amt = models.FloatField(blank=True, null=True)
    percentage = models.IntegerField()
    parent_bucket = models.IntegerField(blank=True, null=True)

class Transaction(models.Model):
    income = models.FloatField()
    date_created =  models.DateTimeField(auto_now_add=True)
    receipt = models.CharField(max_length=5000)

class Icon(models.Model):
    name = models.CharField(max_length=20)
    image = models.URLField()