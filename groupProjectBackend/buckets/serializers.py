from rest_framework import serializers
from .models import Transaction, Bucket, Icon

class TransactionSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    # user_id = serializers.ReadOnlyField (source='user.id')
    income = serializers.FloatField()
    date_created = serializers.ReadOnlyField()
    receipt = serializers.CharField(max_length=5000)

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

class BucketSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=50, required=False)
    is_active = serializers.BooleanField(default=1)
    min_amt = serializers.FloatField(required=False, allow_null=True)
    percentage = serializers.IntegerField()
    parent_bucket = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        return Bucket.objects.create(**validated_data)

class BucketDetailSerializer(BucketSerializer):
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.min_amt = validated_data.get('min_amt', instance.min_amt)
        instance.percentage = validated_data.get('percentage', instance.percentage)
        instance.parent_bucket = validated_data.get('parent_bucket', instance.parent_bucket)
        instance.save()
        return instance
        


class IconSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    image = serializers.CharField()

    def create(self, validated_data):
        return IconSerializer.objects.create(**validated_data)