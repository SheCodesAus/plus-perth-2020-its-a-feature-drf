from django.contrib import admin
from .models import Bucket, Transaction, Icon

@admin.register(Bucket)
class BucketAdmin(admin.ModelAdmin):
    pass
