from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('buckets/', views.BucketList.as_view()),
    path('buckets/<int:pk>/', views.BucketDetail.as_view()),
    path('transactions/', views.TransactionList.as_view()),
    path('transactions/<int:pk>/', views.TransactionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)