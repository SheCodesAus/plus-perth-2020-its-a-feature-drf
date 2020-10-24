from rest_framework import serializers

from .models import Transaction, Bucket


class BucketSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=50)
    is_active = serializers.BooleanField()
    min_amt = serializers.FloatField()
    percentage = serializers.IntegerField()
    parent_bucket = serializers.IntegerField()

    def create(self, validated_data):
        return Bucket.objects.create(**validated_data)


class TransactionSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    income = serializers.FloatField()
    date_created = serializers.ReadOnlyField()
    receipt = serializers.CharField(max_length="5000")

    def create(self, validated_data):

        return Transaction.objects.create(**validated_data)