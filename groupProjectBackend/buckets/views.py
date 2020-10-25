from rest_framework import status, permissions
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction, Bucket, Icon
from .serializers import TransactionSerializer, BucketSerializer, BucketDetailSerializer, IconSerializer

# Create your views here.
class BucketList(APIView):

    def get(self, request):
        buckets = Bucket.objects.all()
        serializer = BucketSerializer(buckets, many=True)
        return Response(serializer.data)

    
    def post(self, request):
        serializer = BucketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(),
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(
          serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class BucketDetail(APIView):

    def get_object(self, pk):
        try:
            return Bucket.objects.get(pk=pk)
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




class TransactionList(APIView):

    # Add permission classes here!!!

    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        
        if serializer.is_valid():
            print(serializer.data)
            serializer.save
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )