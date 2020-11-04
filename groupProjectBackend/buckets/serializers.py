from rest_framework import serializers
from .models import Transaction, Bucket

class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class BucketSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.id')
    
    class Meta:
        model = Bucket
        fields = (
            'id',
            'owner',
            'name',
            'description',
            'icon',
            'is_active',
            'min_amt',
            'percentage',
            'parent_bucket',
            'children'
            )

    def create(self, validated_data):
        return Bucket.objects.create(**validated_data)


class BucketListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = Bucket
        fields = (
            'id',
            'owner',
            'name')

class BucketDetailSerializer(BucketSerializer):

    def update(self, instance, validated_data):        
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.icon = validated_data.get('icon', instance.icon)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.min_amt = validated_data.get('min_amt', instance.min_amt)
        instance.percentage = validated_data.get('percentage', instance.percentage)
        instance.parent_bucket = validated_data.get('parent_bucket', instance.parent_bucket)
        instance.save()
        return instance

class TransactionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField (source='owner.id')
    receipt = serializers.JSONField()
    
    class Meta:
        model = Transaction
        fields = (
            'id',
            'owner',
            'income',
            'date_created',
            'receipt'
            )

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

class TransactionDetailSerializer(TransactionSerializer):

    def update(self, instance, validated_data):        
        instance.income = validated_data.get('income', instance.income)
        instance.receipt = validated_data.get('receipt', instance.receipt)
        instance.save()
        return instance
