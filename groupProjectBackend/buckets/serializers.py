from rest_framework import serializers
from .models import Transaction, Bucket, Expense

class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class ExpenseSerializer(serializers.ModelSerializer):
    bucket_id = serializers.IntegerField()
    bucket_name = serializers.ReadOnlyField(source='bucket.name')
    
    class Meta:
        model = Expense
        fields = (
            'id',
            'bucket_id',
            'bucket_name',
            'name',
            'monthly_exp_amt',            
            )

    def create(self, validated_data):
        return Expense.objects.create(**validated_data)

class ExpenseDetailSerializer(ExpenseSerializer):

    def update(self, instance, validated_data):        
        instance.name = validated_data.get('name', instance.name)
        instance.monthly_exp_amt = validated_data.get('monthly_exp_amt', instance.monthly_exp_amt)
        instance.bucket_id = validated_data.get('bucket_id', instance.bucket_id)
        instance.save()
        return instance

class BucketSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.id')
    # expenses = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    # expenses = serializers.StringRelatedField(many=True)
    expenses = ExpenseSerializer(many=True, read_only=True)

    
    class Meta:
        model = Bucket
        fields = (
            'id',
            'owner',
            'name',
            'description',
            'icon',
            'is_active',            
            'percentage',
            'parent_bucket',
            'min_amt',
            'expenses',
            'children',            
   
            )

    def create(self, validated_data):
        return Bucket.objects.create(**validated_data)


class BucketListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    expenses = serializers.ReadOnlyField(source='expenses.name')
    expenses = Expense
    class Meta:
        model = Bucket
        fields = (
            'id',
            'owner',
            'name',
            'expenses',
            )

class BucketDetailSerializer(BucketSerializer):

    def update(self, instance, validated_data):        
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.icon = validated_data.get('icon', instance.icon)
        instance.is_active = validated_data.get('is_active', instance.is_active)
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


