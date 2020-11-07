from rest_framework import status, permissions
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsOwner
from .models import Transaction, Bucket, Expense
from .serializers import TransactionSerializer, TransactionDetailSerializer, BucketSerializer, BucketDetailSerializer, BucketListSerializer, ExpenseSerializer, ExpenseDetailSerializer

# Create your views here.
class BucketList(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get(self, request):
        buckets = Bucket.objects.filter(owner=request.user, parent_bucket__isnull=True)
        serializer = BucketSerializer(buckets, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BucketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user),
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(
          serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class BucketListDropdown(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get(self, request):
        buckets = Bucket.objects.filter(owner=request.user).order_by('name')
        serializer = BucketListSerializer(buckets, many=True)
        return Response(serializer.data)

class BucketDetail(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_object(self, pk):
        try:
            bucket = Bucket.objects.get(pk=pk)
            self.check_object_permissions(self.request, bucket)
            return bucket
        except Bucket.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        bucket = self.get_object(pk)
        serializers = BucketSerializer(bucket)
        return Response(serializers.data)

    def put(self, request, pk):
        bucket = self.get_object(pk)
        data = request.data
        serializer = BucketDetailSerializer(
            instance=bucket,
            data=data,
            partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


    def delete(self, request, pk ,format=None):
        bucket = self.get_object(pk) 
        bucket.delete()
        return Response("Bucket Tree Deleted", status=status.HTTP_204_NO_CONTENT)



class TransactionList(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get(self, request):
        transactions = Transaction.objects.filter(owner=request.user).order_by('-date_created')
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(owner=request.user),
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class TransactionDetail(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_object(self, pk):
        try:
            transaction = Transaction.objects.get(pk=pk)
            self.check_object_permissions(self.request, transaction)
            return transaction
        except Transaction.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        transaction = self.get_object(pk)
        serializers = TransactionDetailSerializer(transaction)
        return Response(serializers.data)

    def delete(self, request, pk ,format=None):
        transaction = self.get_object(pk)
        transaction.delete()
        return Response("Transaction Deleted", status=status.HTTP_204_NO_CONTENT)


class ExpenseList(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get(self, request):
        expenses = Expense.objects.filter(owner=request.user)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user),
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(
          serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ExpenseDetail(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_object(self, pk):
        try:
            expense = Expense.objects.get(pk=pk)
            self.check_object_permissions(self.request, expense)
            return expense
        except Bucket.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        expense = self.get_object(pk)
        serializers = ExpenseSerializer(expense)
        return Response(serializers.data)

    def put(self, request, pk):
        expense = self.get_object(pk)
        data = request.data
        serializer = ExpenseDetailSerializer(
            instance=expense,
            data=data,
            partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk ,format=None):
        expense = self.get_object(pk) 
        expense.delete()
        return Response("Expense Deleted", status=status.HTTP_204_NO_CONTENT)