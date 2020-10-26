from rest_framework import status, permissions
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsOwner
from .models import Transaction, Bucket, Icon
from .serializers import TransactionSerializer, TransactionDetailSerializer, BucketSerializer, BucketDetailSerializer, IconSerializer

# Create your views here.
class BucketList(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get(self, request):
        # buckets = Bucket.objects.all()
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

class BucketDetail(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)

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
        transactions = Transaction.objects.filter(owner=request.user)
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
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        transaction = self.get_object(pk)
        if transaction.owner == request.user:
            serializers = TransactionDetailSerializer(transaction)
            return Response(serializers.data)
        return Response("Not Authorised")

    def put(self, request, pk):
        transaction = self.get_object(pk)
        if transaction.owner == request.user:
            data = request.data
            serializer = TransactionDetailSerializer(
                instance=transaction,
                data=data,
                partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response("Not Authorised")

    def delete(self, request, pk ,format=None):
        transaction = self.get_object(pk)
        if transaction.owner == request.user:
            transaction.delete()
            return Response("Transaction Deleted", status=status.HTTP_204_NO_CONTENT)
        return Response("Not Authorised")